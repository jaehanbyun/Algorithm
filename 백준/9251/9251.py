import sys

input = sys.stdin.readline

a = list(input().rstrip())
b = list(input().rstrip())
matrix = [[0] * len(a) for _ in range(len(b))]

for i in range(len(a)):
    if b[0] == a[i]:
        for j in range(i, len(a)):
            matrix[0][j] = 1
        break

for i in range(1, len(b)):
    for j in range(len(a)):
        if b[i] == a[j]:
            matrix[i][j] = 1 if j==0 else matrix[i-1][j-1]+1
        else:
            matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

print(matrix[-1][-1])