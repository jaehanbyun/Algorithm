import sys
import heapq

input = sys.stdin.readline

N = int(input())
pq = []

for _ in range(N):
    op = int(input())
    if op != 0:
        heapq.heappush(pq, -op)
    else:
        print(-heapq.heappop(pq) if len(pq) != 0 else 0)
