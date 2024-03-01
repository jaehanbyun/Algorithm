import sys
import heapq

input = sys.stdin.readline

M, N = map(int, input().split())
matrix = [list(map(int, input().rstrip())) for _ in range(N)]
dist = [[int(1e9)] * M for _ in range(N)]

q = []
heapq.heappush(q, (0, 0, 0))

while q:
    cur_dist, x, y = heapq.heappop(q)
    dist[0][0] = 0

    if dist[x][y] < cur_dist:
        continue

    for nx, ny in ((x+1, y), (x, y+1), (x-1, y), (x, y-1)):
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        if cur_dist + matrix[nx][ny] < dist[nx][ny]:
            dist[nx][ny] = cur_dist + matrix[nx][ny]
            heapq.heappush(q, (dist[nx][ny], nx, ny))

print(dist[N-1][M-1])