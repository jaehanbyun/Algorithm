import sys

input = sys.stdin.readline

def check(line):
    for i in range(1, N):
        if abs(line[i] - line[i-1]) > 1:
            return False

        if line[i] > line[i-1]: # 왼쪽 체크
            for j in range(L):
                if i-j-1 < 0 or line[i-1] != line[i-j-1] or visited[i-j-1]:
                    return False
                visited[i-j-1] = True
        elif line[i] < line[i-1]: # 오른쪽 체크
            for j in range(L):
                if i+j >= N or line[i] != line[i+j] or visited[i+j]:
                    return False
                visited[i+j] = True

    return True

N, L = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
rst = 0

for i in range(N):
    visited = [False] * N
    if check(matrix[i]):
        rst += 1

for i in range(N):
    visited = [False] * N
    tmp = [matrix[j][i] for j in range(N)]
    if check(tmp):
        rst += 1

print(rst)