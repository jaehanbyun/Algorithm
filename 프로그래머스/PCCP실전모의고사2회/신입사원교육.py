import heapq

def solution(abiility, number):
    hQ = []
    for em in abiility:
        heapq.heappush(hQ, em)

    while number > 0:
        one = heapq.heappop(hQ)
        two = heapq.heappop(hQ)
        total = one+two

        heapq.heappush(hQ, total)
        heapq.heappush(hQ, total)

        number -= 1

    return sum(hQ)

print(solution([10, 3, 7, 2], 2))