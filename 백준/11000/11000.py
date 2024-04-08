import sys
import heapq

input = sys.stdin.readline

n = int(input())
lectures = [list(map(int, input().split())) for _ in range(n)]

lectures.sort(key=lambda x: (x[0], x[1]))

hq = [lectures[0][1]]

for i in range(1, n):
    if lectures[i][0] >= hq[0]:
        heapq.heappop(hq)
    heapq.heappush(hq, lectures[i][1])

print(len(hq))