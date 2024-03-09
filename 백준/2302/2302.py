import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
case_set = []
matrix = [1] * (N+1)

for _ in range(M):
    fix_seat = int(input())
    matrix[fix_seat] = 0

each_sum = 0
cnt = 0
for i in range(1, N+1):
    if matrix[i] == 0:
        if each_sum > 0:
            case_set.append(each_sum)
            cnt = 0
            each_sum = 0
        continue

    cnt += 1

    if cnt > 2:
        matrix[i] = matrix[i-1] + matrix[i-2]
    else:
        matrix[i] = cnt

    each_sum = matrix[i]

if matrix[N] > 0:
    case_set.append(matrix[N])

rst = 1
for n in case_set:
    rst *= n

print(rst)