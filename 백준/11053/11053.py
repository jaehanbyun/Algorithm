import sys

input = sys.stdin.readline

len_A = int(input())
A = list(map(int, input().split()))

answer = 0
matrix = [1] * len_A

for a in range(1, len_A):
    for b in range(a):
        if A[a] > A[b]:
            matrix[a] = max(matrix[a], matrix[b] + 1)

print(max(matrix))