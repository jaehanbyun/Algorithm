import sys

input = sys.stdin.readline

def check(mid):
    cnt = 0

    for item in j:
        if item % mid != 0:
            cnt += (item//mid) + 1
        else:
            cnt += (item//mid)

    return cnt

n, m = map(int, input().split())
j = [int(input()) for _ in range(m)]
lo, hi = 1, max(j)
answer = 0

while lo <= hi:
    mid = (lo + hi) // 2

    if check(mid) > n:
        lo = mid + 1
    else:
        hi = mid - 1
        answer = mid

print(answer)