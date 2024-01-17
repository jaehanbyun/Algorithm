import sys
from collections import deque

input = sys.stdin.readline

def solution(p, arr):
    queue = deque(arr)
    flag = 0

    for c in p:
        if c == 'R':
            flag = (flag+1)%2
        if c == 'D':
            if len(queue) == 0:
                print('error')
                return
            else:
                if flag%2 == 1:
                    queue.pop()
                else:
                    queue.popleft()

    queue = list(queue) if flag%2 == 0 else list(queue)[::-1]
    print('['+','.join(map(str, queue))+']')

T = int(input())

for _ in range(T):
    p = list(input().strip())
    n = int(input())
    arr = input().strip('[]\n')
    if ',' in arr:
        arr = list(map(int, arr.split(',')))
    else:
        arr = [int(arr)] if len(arr) > 0 else []
    solution(p, arr)