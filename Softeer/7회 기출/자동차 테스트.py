import sys
import bisect

input = sys.stdin.readline

def search(num):
    if num <= cars[0] or cars[-1] <= num:
        return 0

    index = bisect.bisect_left(cars, num)
    if index < n and cars[index] == num:
        f = index
        s = n-index-1
        return f*s
    else:
        return 0

n, q = map(int, input().split())
cars = list(map(int, input().split()))
mid_num = []

for _ in range(q):
    num = int(input())
    mid_num.append(num)

cars.sort()

for k in mid_num:
    answer = search(k)
    print(answer)