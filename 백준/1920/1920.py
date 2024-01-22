import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
X = list(map(int, input().split()))

A.sort()

for x in X:
    start, end = 0, N-1
    flag = 0
    while start <= end:
        mid = (start+end)//2
        if A[mid] < x:
            start = mid + 1
        elif A[mid] > x:
            end = mid - 1
        else:
            flag = 1
            break
    print(1) if flag == 1 else print(0)

