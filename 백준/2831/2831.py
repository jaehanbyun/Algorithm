import sys

input = sys.stdin.readline

n = int(input())
h_m = list(map(int, input().split()))
h_w = list(map(int, input().split()))

pos_men = sorted([m for m in h_m if m > 0])
neg_men = sorted([-m for m in h_m if m < 0])
pos_women = sorted([w for w in h_w if w > 0])
neg_women = sorted([-w for w in h_w if w < 0])

def match_pairs(pos, neg):
    i, j = 0, 0
    cnt = 0

    while i < len(pos) and j < len(neg):
        if pos[i] < neg[j]:
            cnt += 1
            i += 1
            j += 1
        else:
            j += 1

    return cnt

print(match_pairs(pos_men, neg_women) + match_pairs(pos_women, neg_men))