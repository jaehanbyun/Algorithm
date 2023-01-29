answer = 0
def dfs(k, cnt, dungeons, visited):
    global answer
    answer = max(answer, cnt)
    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and visited[i] == 0:
            visited[i] = 1
            dfs(k - dungeons[i][1], cnt + 1, dungeons, visited)
            visited[i] = 0

def solution(k, dungeons):
    visited = [0] * len(dungeons)
    dfs(k, 0, dungeons, visited)
    return answer