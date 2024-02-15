import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
matrix = [[[] for _ in range(N)] for _ in range(N)]
fireballs = []
# 0 ~ 8 방향
direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs.append([r-1, c-1, m, s, d])

for _ in range(K):
    while fireballs:
        cr, cc, cm, cs, cd = fireballs.pop()
        nr = (cr + cs * direction[cd][0]) % N
        nc = (cc + cs * direction[cd][1]) % N
        matrix[nr][nc].append([cm, cs, cd])

    for a in range(N):
        for b in range(N):
            if len(matrix[a][b]) > 1:
                sum_m, sum_s, sum_d, cnt_even, cnt_odd, cnt, nd = 0, 0, 0, 0, 0, len(matrix[a][b]), []
                while matrix[a][b]:
                    cm, cs, cd = matrix[a][b].pop()
                    sum_m += cm
                    sum_s += cs
                    if cd % 2 == 0:
                        cnt_even += 1
                    else:
                        cnt_odd += 1
                if cnt_even == cnt or cnt_odd == cnt:
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]
                if sum_m // 5:
                    for d in nd:
                        fireballs.append([a, b, sum_m//5, sum_s//cnt, d])
            elif len(matrix[a][b]) == 1:
                fireballs.append([a, b] + matrix[a][b].pop())

print(sum(f[2] for f in fireballs))