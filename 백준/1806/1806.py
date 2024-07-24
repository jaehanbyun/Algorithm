import sys

input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
start, end, rst, total = 0, 0, 1e9, arr[0]

while start <= end:
    # print("total:", total, "start:", start, "end:", end)
    if total >= s:
        rst = min(rst, end-start+1)
        total -= arr[start]
        start += 1
    else:
        end += 1
        if end == n:
            break
        total += arr[end]

if rst == 1e9:
    print(0)
else:
    print(rst)