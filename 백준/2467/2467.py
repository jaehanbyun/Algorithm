import sys

input = sys.stdin.readline

N = int(input())
sets = list(map(int, input().split()))

start, end = 0, N-1
gap = float("INF")
final_l, final_r = 0, 0

while start < end:
    tmp = sets[start] + sets[end]

    if abs(tmp) < gap:
        final_l = start
        final_r = end
        gap = abs(tmp)
        if gap == 0:
            break

    if tmp < 0:
        start += 1
    else:
        end -= 1

print(sets[final_l], sets[final_r])