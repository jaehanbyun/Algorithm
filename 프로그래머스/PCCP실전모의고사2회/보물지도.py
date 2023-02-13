from collections import deque
def solution(n, m, hole):
    answer = 0
    table = [[0 for col in range(m + 1)] for row in range(n + 1)]
    dist = [[[-1,-1] for col in range(m + 1)] for row in range(n + 1)]
    h = [-1, 1, 0, 0]
    w = [0, 0, -1, 1]

    dist[1][1][0] = 0

    for a, b in hole:
        table[a][b] = 1

    for i in range(n):
        print(table[i])

    def bfs(table, dist, x, y):
        queue = deque()
        queue.append((x, y))

        while len(queue)!=0:
            x, y = queue.popleft()

    return answer

print(solution(4, 4, [[2, 3], [3, 3]]))