import sys
from collections import deque

input = sys.stdin.readline

def get_loc(x):
    yield x-1
    yield x+1
    yield x*2

N, K = map(int, input().split())
rst = 0
queue = deque()
queue.append((N, 0))
visited = [0] * (10**5+1)

while queue:
    cur, time = queue.popleft()

    if cur == K:
        rst = time
        break

    for next in get_loc(cur):
        if 0 <= next <= 10**5 and visited[next] == 0:
            visited[next] = 1
            queue.append((next, time+1))

print(rst)