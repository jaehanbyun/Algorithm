import sys

input = sys.stdin.readline

def check(mid):
    cnt = 0
    for i in range(len(restarea_pos)-1):
        if restarea_pos[i+1] - restarea_pos[i] > mid:
            cnt += (restarea_pos[i+1] - restarea_pos[i] - 1) // mid

    return cnt

n, m, l = map(int,input().split())

restarea_pos = list(map(int, input().split()))
restarea_pos.append(0)
restarea_pos.append(l)
restarea_pos.sort()

lo, hi = 0, l

while lo + 1 < hi:
    mid = (lo + hi)//2

    if check(mid) > m:
        lo = mid
    else:
        hi = mid

print(hi)