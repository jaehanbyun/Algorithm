import sys
sys.setrecursionlimit(10**4)

input = sys.stdin.readline

def check(r):
    for i in range(r):
        if chess[i] == chess[r] or abs(chess[r] - chess[i]) == abs(r - i):
            return False

    return True

def backtracking(r):
    global rst

    if r == N:
        rst += 1
        return

    for c in range(N):
        chess[r] = c
        if check(r):
            backtracking(r+1)

    return

N = int(input())

chess = [0] * N
rst = 0

backtracking(0)
print(rst)