import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

N, M, X = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    s, d, w = map(int, input().split())
    graph[s].append((w, d))

def search(s):
    pq = []
    costs = [float('inf')] * (N + 1)
    costs[s] = 0
    heapq.heappush(pq, (0, s))

    while pq:
        cur_cost, cur_town = heapq.heappop(pq)

        if cur_cost > costs[cur_town]:
            continue

        for cost, next_town in graph[cur_town]:
            next_cost = cur_cost + cost
            if next_cost < costs[next_town]:
                costs[next_town] = next_cost
                heapq.heappush(pq, (next_cost, next_town))

    return costs

x_to_other_costs = search(X)
ohter_to_x_costs = [0] * (N+1)
answer = 0
for i in range(1, N+1):
    if i != X:
        cost = search(i)
        ohter_to_x_costs[i] = cost[X]
        answer = max(answer, x_to_other_costs[i]+ohter_to_x_costs[i])

print(answer)