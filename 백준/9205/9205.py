import sys
from collections import deque, defaultdict

input = sys.stdin.readline

def check(x1, y1, x2, y2):
    if abs(x2 - x1) + abs(y2 - y1) <= 1000:
        return True
    return False
def solution(n):
    home_x, home_y = map(int, input().split())
    market = [list(map(int, input().split())) for _ in range(n)]
    goal_x, goal_y = map(int, input().split())

    graph = []
    graph.append([home_x, home_y])
    for i in range(n):
        graph.append(market[i])
    graph.append([goal_x, goal_y])
    visited = [False] * (n+2)
    queue = deque()
    queue.append([home_x, home_y, 0])

    while queue:
        cur_x, cur_y, index = queue.popleft()
        visited[index] = True

        if cur_x == goal_x and cur_y == goal_y:
            print('happy')
            return

        for i in range(n+2):
            next_x, next_y = graph[i]
            if visited[i] == False and check(cur_x, cur_y, next_x, next_y):
                queue.append([next_x, next_y, i])

    print('sad')

t = int(input())

for _ in range(t):
    n = int(input())
    solution(n)