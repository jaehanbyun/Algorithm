import sys
import heapq

input = sys.stdin.readline

N = int(input())
cards = []

for _ in range(N):
    num = int(input())
    heapq.heappush(cards, num)

answer = 0
while len(cards) != 1:
    first = heapq.heappop(cards)
    second = heapq.heappop(cards)
    new_deck = first + second
    heapq.heappush(cards, new_deck)
    answer += new_deck

print(answer)