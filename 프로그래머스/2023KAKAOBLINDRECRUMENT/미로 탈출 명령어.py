import sys
sys.setrecursionlimit(10 ** 6)

def oob(x, y, n, m):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    return True


def solution(n, m, x, y, r, c, k):
    answer = 'z'
    dir = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    command = ['d', 'l', 'r', 'u']

    def backtracking(depth, cx, cy, cur_route):
        nonlocal answer
        if k < depth + abs(r - cx - 1) + abs(c - cy - 1):
            return

        if depth == k:
            if cx == r - 1 and cy == c - 1:
                answer = cur_route
            return

        for i in range(4):
            nx = cx + dir[i][0]
            ny = cy + dir[i][1]

            if oob(nx, ny, n, m) and cur_route < answer:
                backtracking(depth + 1, nx, ny, cur_route + command[i])

    if (k - (abs(r - x) + abs(c - y))) % 2 == 1 or (abs(r - x) + abs(c - y)) > k:
        answer = 'impossible'
    else:
        backtracking(0, x - 1, y - 1, '')

    return answer