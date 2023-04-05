import sys
import heapq

num = int(input())

def solution(q, arr, hQ):
    cnt = 0

    while len(arr)!=0:
        if arr[0][1] >= -hQ[0]:
            heapq.heappop(hQ)
            check = arr[0][0]
            cnt+=1
            if check==q:
                return cnt
            del arr[0]
        else:
            arr.append(arr[0])
            del arr[0]
    return cnt

for i in range(num):
    docnum, q = map(int, sys.stdin.readline().split())
    priority = list(map(int, sys.stdin.readline().split()))
    arr = []
    hQ = []
    for i in range(docnum):
        arr.append((i, priority[i]))
        heapq.heappush(hQ, -priority[i])

    answer = solution(q, arr, hQ)

    print(answer)