import sys

input = sys.stdin.readline

def solution(x1, y1, x2, y2):
    return matrix[x2][y2] - matrix[x2][y1-1] - matrix[x1-1][y2] + matrix[x1-1][y1-1]

N, M = map(int, input().split())
matrix = [[0] * (N+1)]

for _ in range(N):
    r = [0]
    r.extend(list(map(int, input().split())))
    matrix.append(r)

for i in range(N+1):
    for j in range(1, N+1):
        matrix[i][j] += matrix[i][j - 1]

for i in range(N+1):
    for j in range(1, N+1):
        matrix[j][i] += matrix[j - 1][i]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    answer = solution(x1, y1, x2, y2)
    print(answer)