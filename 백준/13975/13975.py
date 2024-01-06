import sys
import heapq

input = sys.stdin.readline

def solution(chapter_len):
    heapq.heapify(chapter_len)
    answer = 0

    while len(chapter_len) != 1:
        first = heapq.heappop(chapter_len)
        second = heapq.heappop(chapter_len)
        new_chapter = first + second
        heapq.heappush(chapter_len, new_chapter)
        answer += new_chapter

    print(answer)

T = int(input())

for _ in range(T):
    K = int(input())
    chapter_len = list(map(int, input().split()))
    solution(chapter_len)