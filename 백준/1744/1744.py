import sys

N = int(sys.stdin.readline())
neg_nums = []
pos_nums = []
answer = 0

for _ in range(N):
    num = int(sys.stdin.readline())
    if num > 1:
        pos_nums.append(num)
    elif num <= 0:
        neg_nums.append(num)
    else:
        answer += num

neg_nums = sorted(neg_nums)
pos_nums = sorted(pos_nums, reverse=True)

for i in range(0, len(pos_nums), 2):
    if i+1 >= len(pos_nums):
        answer += pos_nums[i]
    else:
        answer += pos_nums[i] * pos_nums[i+1]

for i in range(0, len(neg_nums), 2):
    if i+1 >= len(neg_nums):
        answer += neg_nums[i]
    else:
        answer += neg_nums[i] * neg_nums[i+1]

print(answer)