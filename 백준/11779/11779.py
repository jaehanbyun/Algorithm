import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수

graph = defaultdict(list)
for _ in range(m):
    s, d, w = map(int, input().split())
    graph[s].append((w, d))

s_city, d_city = map(int, input().split())
pq = []
costs = [float('inf')] * (n + 1)
costs[s_city] = 0
parents = [0] * (n + 1)
heapq.heappush(pq, (0, s_city))

while pq:
    cur_cost, cur_city = heapq.heappop(pq)

    if cur_city == d_city:
        break

    if cur_cost > costs[cur_city]:
        continue

    for cost, next_city in graph[cur_city]:
        next_cost = cur_cost + cost
        if next_cost < costs[next_city]:
            costs[next_city] = next_cost
            parents[next_city] = cur_city
            heapq.heappush(pq, (next_cost, next_city))

path = []
tmp = d_city
while tmp != s_city:
    path.append(tmp)
    tmp = parents[tmp]
path.append(s_city)

print(costs[d_city])
print(len(path))
path.reverse()
print(*path)