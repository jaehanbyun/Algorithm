import sys

n, k = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

gap = []

for i in range(n-1):
    gap.append(arr[i+1]-arr[i])

gap.sort(reverse=True)

# 큰 순서의 차이 k-1개를 배열에서 없애고 sum을 구하려고 했으나,
# 시간초과가 났음. => 해당 과정 생략 후 리스트 슬라과싱으로 값 도출 시 통
# for i in range(k-1):
#     del gap[0]

print(sum(gap[k-1:]))



