import sys

input = sys.stdin.readline

n = int(input())
towers = list(map(int, input().split()))
stack = []
answer = []

for idx, v in enumerate(towers):
    while stack:
        if stack[-1][0] > v:
            answer.append(stack[-1][1])
            break
        else:
            stack.pop()

    if not stack:
        answer.append(0)
    stack.append((v, idx+1))

print(*answer)