# import sys
# from itertools import permutations
#
# input = sys.stdin.readline
#
# N = int(input())
# A = list(map(int, input().split()))
# op_num1 = list(map(int, input().split()))
# op_num2 = []
#
# max_rst = -float('inf')
# min_rst = float('inf')
#
# for i in range(4):
#     for _ in range(op_num1[i]):
#         op_num2.append(i)
#
# for k in permutations(op_num2):
#     tmp = A[0]
#     for i in range(N-1):
#         if k[i] == 0:
#             tmp += A[i+1]
#         elif k[i] == 1:
#             tmp -= A[i+1]
#         elif k[i] == 2:
#             tmp *= A[i+1]
#         else:
#             if tmp < 0:
#                 tmp = -((-tmp) // A[i+1])
#             else:
#                 tmp //= A[i+1]
#
#     max_rst = max(max_rst, tmp)
#     min_rst = min(min_rst, tmp)
#
# print(max_rst)
# print(min_rst)

import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
op_num1 = list(map(int, input().split()))

max_rst = -float('inf')
min_rst = float('inf')

def dfs(depth, sum, plus, minus, multiply, divide):
    global max_rst, min_rst
    if depth == N:
        max_rst = max(max_rst, sum)
        min_rst = min(min_rst, sum)

    if plus:
        dfs(depth+1, sum+A[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, sum - A[depth], plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth+1, sum*A[depth], plus, minus, multiply-1, divide)
    if divide:
        dfs(depth+1, int(sum/A[depth]), plus, minus, multiply, divide-1)

dfs(1, A[0], op_num1[0], op_num1[1], op_num1[2], op_num1[3])
print(max_rst)
print(min_rst)