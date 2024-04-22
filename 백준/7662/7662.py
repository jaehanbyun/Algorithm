import sys
import heapq

input = sys.stdin.readline

def solution(k: int):
    minhq = []
    maxhq = []
    check = [1] * k

    for i in range(k):
        o, n = input().split()
        n = int(n)

        if o == 'I':
            heapq.heappush(maxhq, (-n, i))
            heapq.heappush(minhq, (n, i))
        else:
            if n == 1:
                if maxhq:
                    check[heapq.heappop(maxhq)[1]] = 0
            else:
                if minhq:
                    check[heapq.heappop(minhq)[1]] = 0

        while maxhq and not check[maxhq[0][1]]:
            heapq.heappop(maxhq)

        while minhq and not check[minhq[0][1]]:
            heapq.heappop(minhq)

    if minhq:
        print(-maxhq[0][0], minhq[0][0])
    else:
        print('EMPTY')

t = int(input())

for _ in range(t):
    k = int(input())
    solution(k)