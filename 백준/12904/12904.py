import sys

# 백트래킹 방식으로 해결 => 시간초과
# def stringOperation(s, l):
#     if len(s) > len(l):
#         return
#     if s == l:
#         global answer
#         answer = 1
#         return
#
#     gap = len(l) - len(s)
#     for _ in range(gap):
#         stringOperation(s+'A', l)
#         s = ''.join(reversed(list(s))) + 'B'
#         stringOperation(s, l)
#
# S = sys.stdin.readline().strip()
# T = sys.stdin.readline().strip()
# answer = 0
#
# stringOperation(S, T)
# print(answer)


def stringOperation(s, t):
    while len(s) < len(t):
        if t[-1] == "A":
            t.pop()
        elif t[-1] == "B":
            t.pop()
            t.reverse()

    if s == t:
        return 1
    else:
        return 0

S = list(map(str, sys.stdin.readline().strip()))
T = list(map(str, sys.stdin.readline().strip()))
answer = stringOperation(S, T)

print(answer)
