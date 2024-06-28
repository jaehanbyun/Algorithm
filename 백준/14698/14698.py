import sys
import heapq

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = 1

    if len(arr) == 1:
        print(answer)
        continue
    else:
        heapq.heapify(arr)

        while len(arr) != 1:
            f = heapq.heappop(arr)
            s = heapq.heappop(arr)
            new_item = f * s
            answer *= new_item
            heapq.heappush(arr, new_item)

        print(answer%1000000007)