import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
answer = [-1] * n
stack = []

stack.append(0)
for i in range(1, n):
    while stack and a[stack[-1]] < a[i]:
        answer[stack.pop()] = a[i]

    stack.append(i)

print(*answer)