import sys
import heapq

input = sys.stdin.readline

n = int(input())
lectures = []
room = []
answer = 0

for _ in range(n):
    a, b, c = map(int, input().split())
    heapq.heappush(lectures, (b, c))

while lectures:
    s, e = heapq.heappop(lectures)

    if not room or room[0][0] > s:
        heapq.heappush(room, (e, s))
    else:
        heapq.heappop(room)
        heapq.heappush(room, (e, s))

    answer = max(answer, len(room))

print(answer)