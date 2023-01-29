cnt = 0
solgap = 100

def dfs(v, graph, visited):
    visited[v] = 1
    global cnt
    cnt += 1
    for node in graph[v]:
        if visited[node] == 0:
            visited[node] = 1
            dfs(node, graph, visited)

def solution(n, wires):
    graph = [[] for _ in range(n)]
    div = n//2
    answer = 0
    global cnt, solgap

    for a, b in wires:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    for it in wires:
        visited = [0]*n
        visited[it[1] - 1] = 1
        cnt = 0
        dfs(it[0] - 1, graph, visited)
        part1 = cnt
        gap = abs(part1 - div)
        if solgap > gap:
            solgap = gap
            answer = abs(part1-(n-part1))
    return answer

