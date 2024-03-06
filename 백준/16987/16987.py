import sys

input = sys.stdin.readline

def search(index):
    global rst

    if index == N:
        tmp = t.count(0)
        rst = max(rst, tmp)
        return

    cur_t, cur_w = t[index], w[index]

    if cur_t == 0:
        search(index+1)
        return

    check = True
    for i in range(N):
        if i == index:
            continue
        if t[i] > 0:
            check = False
            break

    if check:
        rst = max(rst, N - 1)
        return

    for i in range(N):
        if i != index and t[i] != 0:
            tmp_t2 = t[i]
            t[index] = t[index] - w[i] if t[index] - w[i] > 0 else 0
            t[i] = t[i] - w[index] if t[i] - w[index] > 0 else 0
            search(index+1)
            t[index] = cur_t
            t[i] = tmp_t2

    return

N = int(input())
t = []
w = []
rst = 0

for _ in range(N):
    t_e, w_e = map(int, input().split())
    t.append(t_e)
    w.append(w_e)

search(0)
print(rst)