낭import sys

N, K = map(int, sys.stdin.readline().split())

temp = [[0,0]]
dp_array = [[0 for _ in range(K+1)] for _ in range(N+1)]

for _ in range(N):
    temp.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        w = temp[i][0]
        v = temp[i][1]

        if j < w:
            dp_array[i][j] = dp_array[i-1][j]
        else:
            dp_array[i][j] = max(dp_array[i-1][j], v+dp_array[i-1][j-w])

print(dp_array[N][K])