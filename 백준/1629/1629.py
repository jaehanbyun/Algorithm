import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

A, B, C = map(int, input().split())

def solution(a, b):
    if b == 1:
        return a % C

    tmp = solution(a, b//2)

    if b%2 == 0:
        return tmp * tmp % C
    else:
        return a * tmp * tmp % C

print(solution(A, B))