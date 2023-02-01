fScore = 0
fLev = 0

def dfs(score, lev, ability, visited):
    global fScore
    global fLev
    fScore = max(score, fScore)

    if lev == fLev:
        return
    for i in range(len(ability)):
        if visited[i] == 0:
            visited[i] = 1
            score += ability[i][lev]
            dfs(score, lev + 1, ability, visited)
            visited[i] = 0
            score -= ability[i][lev]

def solution(ability):
    global fScore
    global fLev
    fLev = len(ability[0])
    visited = [0] * len(ability)
    dfs(0, 0, ability, visited)

    return fScore
