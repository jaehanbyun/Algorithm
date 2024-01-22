import sys

input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))

sorted_X = sorted(list(set(X)))
dict = {}

for i, v in enumerate(sorted_X):
    dict[v] = i

for i in range(N):
    print(dict[X[i]], end=' ')