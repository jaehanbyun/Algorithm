import sys
from collections import deque

input = sys.stdin.readline

def func_D(n):
    return (2 * n) % 10000

def func_S(n):
    return (n - 1) % 10000 if n != 0 else 9999

def func_L(n):
    d1 = n // 1000
    d234 = n % 1000
    return (d234 * 10) + d1

def func_R(n):
    d4 = n % 10
    d123 = n // 10
    return (d4 * 1000) + d123

t = int(input().strip())

for _ in range(t):
    a, b = map(int, input().strip().split())
    visited = [False] * 10000
    queue = deque([(a, '')])
    visited[a] = True

    while queue:
        num, com = queue.popleft()

        if num == b:
            print(com)
            break

        for c, func in (('D', func_D), ('S', func_S), ('L', func_L), ('R', func_R)):
            next_num = func(num)
            if not visited[next_num]:
                visited[next_num] = True
                queue.append((next_num, com + c))