import sys

input = sys.stdin.readline

def backtracking(index, alpha, count, num1, num2):
    if count == L and num1 >= 1 and num2 >= 2:
        print(alpha)
        return

    for i in range(index+1, C):
        if visited[i] == 0:
            tmp1, tmp2 = num1, num2
            if alphabets[i] in sets:
                num1 += 1
            else:
                num2 += 1
            visited[i] = 1
            backtracking(i, alpha+alphabets[i], count+1, num1, num2)
            visited[i] = 0
            num1, num2 = tmp1, tmp2

    return

L, C = map(int, input().split())
alphabets = list(map(str, input().split()))
alphabets.sort()

visited = [0] * C
sets = ['a', 'e', 'i', 'o', 'u']
for i, a in enumerate(alphabets):
    num1, num2 = 0, 0
    visited[i] = 1
    if a in sets:
        num1 += 1
    else:
        num2 += 1
    backtracking(i, a, 1, num1, num2)
    visited[i] = 0