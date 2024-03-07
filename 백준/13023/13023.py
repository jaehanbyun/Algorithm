import sys
from collections import defaultdict

input = sys.stdin.readline

def backtracking(f_num, fG):
    global flag
    if len(fG) == 5:
        flag = 1
        return

    for f in friends[f_num]:
        if f not in fG:
            fG.add(f)
            backtracking(f, fG)
            fG.remove(f)

    return

N, M = map(int, input().split())
friends = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

flag = 0
for f_num in range(N):
    fG = set()
    fG.add(f_num)
    backtracking(f_num, fG)
    if flag == 1:
        print(1)
        break
else:
    print(0)