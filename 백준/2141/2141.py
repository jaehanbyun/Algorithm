import sys

input = sys.stdin.readline

n = int(input())
town = []
sum_people, tmp, mid, num = 0, 0, 0, 0

for _ in range(n):
    x, a = map(int, input().split())
    town.append((x, a))
    sum_people += a

town.sort(key=lambda x: x[0])

mid = (sum_people+1)//2

for i in range(n):
    tmp += town[i][1]

    if mid <= tmp:
        num = town[i][0]
        break

print(num)