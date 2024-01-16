import sys

input = sys.stdin.readline

target_channel = int(input())
broken_num = int(input())
broken_button = list(map(int, input().split())) if broken_num > 0 else []

cur_channel = 100
avail_num = [n for n in range(10)]
min_cnt = abs(target_channel - 100)

for i in broken_button:
    avail_num.remove(i)

for n in range(1000000):
    num = str(n)
    for i in range(len(num)):
        if int(num[i]) not in avail_num:
            break
        if i == len(num)-1:
            min_cnt = min(min_cnt, abs(int(num)-target_channel)+len(num))

print(min_cnt)