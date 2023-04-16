import sys
import heapq

n = int(sys.stdin.readline())
hQ = []

for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    heapq.heappush(hQ, (s, e))

room = [0]
answer = 0
for i in range(n):
    meet = heapq.heappop(hQ)
    # 이중 for문으로 회의실을 찾아서 시간 초과 => 우선순위큐로 변경
    if room[0] <= meet[0] :
        heapq.heappop(room)
        heapq.heappush(room, meet[1])
    else:
        heapq.heappush(room, meet[1])

    if answer < len(room):
        answer = len(room)

print(answer)
