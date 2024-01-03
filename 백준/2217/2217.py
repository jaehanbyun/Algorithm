import sys

input = sys.stdin.readline

N = int(input())
rope = [int(input()) for _ in range(N)]

rope.sort(reverse=True)

answer = 0
for i in range(N):
    temp_answer = rope[i] * (i+1)
    answer = max(answer, temp_answer)

print(answer)