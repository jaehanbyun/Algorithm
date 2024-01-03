import sys

input = sys.stdin.readline

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x: (x[1], x[0]))

answer = 0
t = 0
for i in range(N):
    if meetings[i][0] < t:
        continue
    answer += 1
    t = meetings[i][1]

print(answer)