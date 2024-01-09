import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

N = int(input()) # 도시의 개수
M = int(input()) # 버스의 개수

graph = defaultdict(list)
for _ in range(M):
    s, d, w = map(int, input().split())
    graph[s].append((w, d))

s_city, d_city = map(int, input().split())
pq = []
costs = {}
heapq.heappush(pq, (0, s_city))

while pq:
    cur_cost, cur_city = heapq.heappop(pq)

    if cur_city not in costs:
        costs[cur_city] = cur_cost
        for cost, next_city in graph[cur_city]:
            next_cost = cur_cost + cost
            heapq.heappush(pq, (next_cost, next_city))

print(costs[d_city])