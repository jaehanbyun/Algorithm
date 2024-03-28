import sys

input = sys.stdin.readline

def check(arr, i):
    if len(arr) == 1:
        return 1
    elif arr[-2] > i:
        return 1
    else:
        return 0
def dfs(depth):
    for i in range(10):
        num.append(i)
        if check(num, i):
            dec_set.append(int(''.join(map(str, num))))
            dfs(depth+1)
        num.pop()
    return


n = int(input())
num = []
dec_set = []

dfs(0)
dec_set.sort()

if n >= len(dec_set):
    print(-1)
else:
    print(dec_set[n])