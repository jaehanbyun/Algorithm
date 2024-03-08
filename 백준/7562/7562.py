import sys
from collections import deque

input = sys.stdin.readline

def outOfBound(loc, l):
    if loc[0] < 0 or loc[0] >= l or loc[1] < 0 or loc[1] >= l:
        return False
    return True

T = int(input())
dir = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]

for _ in range(T):
    l = int(input())
    cur_loc = list(map(int, input().split()))
    tar_loc = list(map(int, input().split()))
    visited = [[0] * l for _ in range(l)]
    visited[cur_loc[0]][cur_loc[1]] = 1
    rst = 0

    queue = deque()
    queue.append([cur_loc, 0])

    while queue:
        cur_loc, cnt = queue.popleft()

        if cur_loc == tar_loc:
            rst = cnt
            break

        for d in dir:
            new_loc = [cur_loc[0] + d[0], cur_loc[1] + d[1]]

            if outOfBound(new_loc, l) == False or visited[new_loc[0]][new_loc[1]] == 1:
                continue

            queue.append([new_loc, cnt+1])
            visited[new_loc[0]][new_loc[1]] = 1

    print(rst)