import sys
from collections import defaultdict

input = sys.stdin.readline

def find_parent(a):
    if parents[a] == a:
        return a

    parents[a] = find_parent(parents[a])
    return parents[a]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a > b:
        parents[a] = b
    else:
        parents[b] = a

n = int(input())
m = int(input())
parents = [0] * (n+1)
edges = []
answer = 0

for i in range(1, n+1):
    parents[i] = i

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort(key=lambda x: x[0])

for cost, a, b in edges:
    if find_parent(a) != find_parent(b):
        union(a, b)
        answer += cost

print(answer)