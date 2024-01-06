import sys
import heapq

input = sys.stdin.readline

N = int(input())
nums = []
lefthq, righthq = [], []  # 최대 힙, 최소 힙

for _ in range(N):
    num = int(input())

    if len(lefthq) == len(righthq):
        heapq.heappush(lefthq, -num)
    else:
        heapq.heappush(righthq, num)

    if righthq and -lefthq[0] > righthq[0]:
        l = heapq.heappop(lefthq)
        r = heapq.heappop(righthq)

        heapq.heappush(lefthq, -r)
        heapq.heappush(righthq, -l)

    print(-lefthq[0])