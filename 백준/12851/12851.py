import sys
from collections import deque

input = sys.stdin.readline

def move(k):
    yield k-1
    yield k+1
    yield k*2

def bfs(u, v):
    queue = deque()
    queue.append(u)
    count, min_cost = 0, 0
    cost[u] = 0

    while queue:
        cur_x = queue.popleft()

        temp = cost[cur_x]
        if cur_x == v:
            min_cost = temp
            count += 1
            continue

        for next_x in move(cur_x):
            if 0 <= next_x <= 100000 and (cost[next_x] == 0 or cost[next_x] == cost[cur_x] + 1):
                cost[next_x] = cost[cur_x] + 1
                queue.append(next_x)

    return count, min_cost

N, K = map(int, input().split())
cost = [0] * 100001
count, min_cost = bfs(N, K)
print(min_cost)
print(count)