import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

V, E = map(int, input().split())
start_node = int(input())
graph = defaultdict(list)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

pq = []
costs = {}
heapq.heappush(pq, (0, start_node))

while pq:
    cur_cost, cur_node = heapq.heappop(pq)

    if cur_node not in costs:
        costs[cur_node] = cur_cost
        for cost, next_node in graph[cur_node]:
            next_cost = cur_cost + cost
            heapq.heappush(pq, (next_cost, next_node))

for i in range(1, V+1):
    if i not in costs:
        print("INF")
    else:
        print(costs[i])