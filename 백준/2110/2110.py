import sys

input = sys.stdin.readline

def check(mid):
    cur_pos = 0
    cnt = 1

    for i in range(1, n):
        if pos[i] >= pos[cur_pos] + mid:
            cnt += 1
            cur_pos = i

    return cnt

n, c = map(int, input().split())
pos = [int(input()) for _ in range(n)]
pos.sort()

lo, hi = 1, pos[-1] - pos[0]
answer = 0

while lo <= hi:
    mid = (lo + hi) // 2

    if check(mid) >= c:
        answer = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(answer)