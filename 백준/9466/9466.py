import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    choice = [0] + list(map(int, input().split()))
    visited = [False] * (n+1)
    num = 0

    def dfs(i):
        global num
        visited[i] = True
        team.append(i)
        next = choice[i]

        if visited[next]:
            if next in team:
                num += len(team[team.index(next):])
        else:
            dfs(next)

    for i in range(1, n+1):
        if not visited[i]:
            team = []
            dfs(i)

    print(n - num)