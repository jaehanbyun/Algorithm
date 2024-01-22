import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

def get_dist(node):
    queue = []
    heapq.heappush(queue, (0, node))
    costs = [INF] * (N+1)

    while queue:
        cur_cost, cur_node = heapq.heappop(queue)

        if costs[cur_node] == INF:
            costs[cur_node] = cur_cost
            for cost, next_node in graph[cur_node]:
                next_cost = cur_cost + cost
                heapq.heappush(queue, (next_cost, next_node))
    return costs

N, E = map(int, input().split())
graph = defaultdict(list)

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

v1, v2 = map(int, input().split())
INF = int(1e9)

first = get_dist(1)
second = get_dist(v1)
third = get_dist(v2)
total_dist1 = 0
total_dist2 = 0

total_dist1 += first[v1]
total_dist1 += second[v2]
total_dist1 += third[N]

total_dist2 += first[v2]
total_dist2 += third[v1]
total_dist2 += second[N]

if total_dist1 >= INF and total_dist2 >= INF:
    print(-1)
else:
    print(total_dist1) if total_dist1 < total_dist2 else print(total_dist2)