N = int(input())
B = [int(x) for x in input().split(' ')]
maxB = int(input())
answer = 0

if sum(B) <= maxB:
    print(max(B))
else:
    start = 0
    end = max(B)
    while start <= end:
        totalB = 0
        mid = (start + end)//2
        for n in B:
            if n <= mid:
                totalB += n
            else:
                totalB += mid
        if totalB <= maxB:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
    print(answer)
