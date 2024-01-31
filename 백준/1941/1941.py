import sys

input = sys.stdin.readline

def backtracking(sets, s_cnt, y_cnt):
    global answer

    if y_cnt > 3:
        return

    if s_cnt+y_cnt==7 and s_cnt >= 4:
        tmp = tuple(sorted(sets))
        if tmp not in history:
            answer += 1
            history.add(tmp)
        return

    for s in sets:
        x = s[0]
        y = s[1]
        for d in dxy:
            nx = x + d[0]
            ny = y + d[1]
            if (0 <= nx < 5) and (0 <= ny < 5) and (nx, ny) not in sets:
                if students[nx][ny] == 'S':
                    backtracking(sets + [(nx, ny)], s_cnt+1, y_cnt)
                else:
                    backtracking(sets + [(nx, ny)], s_cnt, y_cnt+1)

students = []
for _ in range(5):
    students.append(list(input().rstrip()))

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = [[False] * 5 for _ in range(5)]
history = set()
answer = 0
for i in range(5):
    for j in range(5):
        if students[i][j] == 'S':
            backtracking([(i, j)], 1, 0)

print(answer)