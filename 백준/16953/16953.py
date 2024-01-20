import sys
from collections import deque

input = sys.stdin.readline

def operation(num):
    return num*2, int(str(num)+'1')

def bfs(a, b):
    global answer
    queue = deque()
    queue.append((a, 1))

    while queue:
        num, count = queue.popleft()
        n1, n2 = operation(num)

        if n1 == b or n2 == b:
            answer = min(answer, count)
            break

        if n1 < b:
            queue.append((n1, count+1))

        if n2 < b:
            queue.append((n2, count+1))

A, B = map(int, input().split())

answer = 1e9
bfs(A, B)
if answer != 1e9:
    print(answer+1)
else:
    print(-1)