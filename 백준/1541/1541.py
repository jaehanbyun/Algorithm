import sys

input = sys.stdin.readline

raw_expression = input().strip().split('-')
final_nums = []
for i in range(len(raw_expression)):
    new_expression = raw_expression[i].split('+')
    sum_nums = sum(map(int, new_expression))
    final_nums.append(sum_nums)

if len(final_nums) == 1:
    print(final_nums[0])
else:
    answer = final_nums[0]
    for i in range(1, len(final_nums)):
        answer -= final_nums[i]
    print(answer)