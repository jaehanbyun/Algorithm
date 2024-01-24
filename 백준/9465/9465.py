import sys

input = sys.stdin.readline

def solution(n, desk):
    for i in range(1, n):
        for j in range(2):
            k = (j+1)%2
            if i >= 2:
                desk[j][i] += max(desk[k][i-1], desk[k][i-2])
            else:
                desk[j][i] += desk[k][i-1]

    return max(desk[0][-1], desk[1][-1])

T = int(input())

for _ in range(T):
    n = int(input())
    desk = []
    for _ in range(2):
        desk.append(list(map(int, input().split())))
    answer = solution(n, desk)
    print(answer)