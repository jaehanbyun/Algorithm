import sys

n = int(sys.stdin.readline())

arr = [0]

for _ in range(n):
    num = int(sys.stdin.readline())
    arr.append(num)

answer = set()

def dfs(i, f, s):
    f.add(i)
    s.add(arr[i])
    if arr[i] in f:
        if f == s:
            answer.update(f)
        return
    return dfs(arr[i], f, s)

for i in range(1, n+1):
    if i not in answer:
        dfs(i, set(), set())

print(len(answer))

answer = sorted(list(answer))
for num in answer:
    print(num)