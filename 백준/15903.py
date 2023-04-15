import sys
import heapq

n, m = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

heapq.heapify(arr)

for i in range(m):
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    newit = a+b
    heapq.heappush(arr, newit)
    heapq.heappush(arr, newit)

print(sum(arr))