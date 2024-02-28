import sys

input = sys.stdin.readline

def OOB(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False

    return True

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
direction = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

for t in range(M):
    d, s = map(int, input().split())
    visited = [[False] * N for _ in range(N)]
    cloud2 = []

    for i in range(len(cloud)):
        x, y = cloud[i]
        nx = (x + direction[d-1][0] * s) % N
        ny = (y + direction[d-1][1] * s) % N

        matrix[nx][ny] += 1
        visited[nx][ny] = True
        cloud2.append((nx, ny))

    for i in range(len(cloud2)):
        x, y = cloud2[i]
        cnt = 0

        for nx, ny in ((x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)):
            if OOB(nx, ny):
                if matrix[nx][ny] > 0:
                    cnt += 1

        matrix[x][y] += cnt

    candidate = []
    for x in range(N):
        for y in range(N):
            if matrix[x][y] >= 2 and visited[x][y] == False:
                matrix[x][y] -= 2
                candidate.append((x, y))

    cloud = candidate

print(sum(map(sum, matrix)))