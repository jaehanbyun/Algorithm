import sys

input = sys.stdin.readline

N = int(input())
drawing_lines = []

# tuple
for _ in range(N):
    drawing_lines.append(tuple(map(int, input().split())))

# list
# for _ in range(N):
#     drawing_lines.append(list(map(int, input().split())))

drawing_lines.sort(key=lambda x: (x[0], x[1]))
start = drawing_lines[0][0]
end = drawing_lines[0][1]
answer = 0

'''
경우 1.      -----
        -----

경우 2.     ------
            -----
            
경우 3.  -----
                -----
'''

for i in range(1, N):
    if drawing_lines[i][1] <= end:
        continue
    elif start <= drawing_lines[i][0] <= end:
        end = drawing_lines[i][1]
    elif end < drawing_lines[i][0]:
        answer += end - start
        start = drawing_lines[i][0]
        end = drawing_lines[i][1]

answer += end - start
print(answer)