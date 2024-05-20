import sys

input = sys.stdin.readline

def check(mid):
    total, cnt = 0, 1

    for item in len_lec:
        if total + item > mid:
            cnt += 1
            total = 0
        total += item

    return cnt

n, m = map(int, input().split())
len_lec = list(map(int, input().split()))
lo, hi = max(len_lec), sum(len_lec)
answer = 0

while lo <= hi:
    mid = (lo + hi) // 2

    if check(mid) > m:
        lo = mid + 1
    else:
        hi = mid - 1
        answer = mid

print(answer)