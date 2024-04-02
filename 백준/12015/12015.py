import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
lis = []

def find_place(num):
    lo, hi = -1, len(lis)

    while lo + 1 < hi:
        mid = (lo+hi)//2

        if not lis[mid] >= num:
            lo = mid
        else:
            hi = mid

    return hi

lis.append(a[0])

for i in a:
    if lis[-1] < i:
        lis.append(i)
    else:
        idx = find_place(i)
        lis[idx] = i

print(len(lis))