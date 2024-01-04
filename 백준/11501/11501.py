import sys

input = sys.stdin.readline

N= int(input())

def solution(days, stat):
    answer = 0
    max_value = stat[-1]

    for i in range(days-2, -1, -1):
        if stat[i] > max_value:
            max_value = stat[i]
        else:
            answer += max_value - stat[i]

    print(answer)

for _ in range(N):
    days = int(input())
    stat = list(map(int, input().split()))
    solution(days, stat)