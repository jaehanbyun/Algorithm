import heapq

def solution(abiility, number):
    heapq.heapify(abiility)

    while number > 0:
        one = heapq.heappop(abiility)
        two = heapq.heappop(abiility)
        total = one+two

        heapq.heappush(abiility, total)
        heapq.heappush(abiility, total)

        number -= 1

    return sum(abiility)

print(solution([10, 3, 7, 2], 2))