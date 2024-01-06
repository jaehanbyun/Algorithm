import sys
import heapq

input = sys.stdin.readline

N = int(input())
questions = []

for _ in range(N):
    deadline, ramen = map(int, input().split())
    questions.append([deadline, ramen])

questions.sort(key=lambda x: x[0])

hq = []

for deadline, ramen in questions:
    heapq.heappush(hq, ramen)

    if len(hq) > deadline:
        heapq.heappop(hq)

print(sum(hq))