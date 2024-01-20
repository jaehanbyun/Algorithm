import copy
import sys

input = sys.stdin.readline

def solution(a, b):
    count = 0
    a_copy = copy.deepcopy(a)

    for i in range(1, N):
        if a_copy[i-1] == b[i-1]:
            continue
        count += 1
        for j in range(i-1, i+2):
            if j < N:
                a_copy[j] = 1 - a_copy[j]

    if a_copy == b:
        return count
    else:
        return 1e9

N = int(input())

cur_state = list(map(int, input().rstrip()))
target_state = list(map(int, input().rstrip()))

answer1 = solution(cur_state, target_state)
cur_state[0] = 1 - cur_state[0]
cur_state[1] = 1 - cur_state[1]
answer2 = solution(cur_state, target_state)+1

final_answer = min(answer1, answer2)

if final_answer != 1e9:
    print(final_answer)
else:
    print(-1)