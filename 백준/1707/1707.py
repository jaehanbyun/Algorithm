import sys
from collections import defaultdict, deque

input = sys.stdin.readline

def solution(V, E):
    graph = defaultdict(list)
    color = [0] * (V+1)

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    queue = deque()

    for i in range(1, V+1):
        if color[i]:
            continue

        color[i] = 1
        queue.append(i)

        while queue:
            cur_v = queue.popleft()
            next_color = color[cur_v]%2 + 1

            for next_v in graph[cur_v]:
                if color[next_v] == 0:
                    color[next_v] = next_color
                    queue.append(next_v)
                elif color[next_v] != next_color:
                    print("NO")
                    return

    print("YES")
    return

K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    solution(V, E)
else:
    print("ji")

