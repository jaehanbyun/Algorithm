import copy
import sys
from collections import defaultdict

input = sys.stdin.readline

def OOB(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return True
    return False
def assign_seat(s_num, friends):
    already_seat = []
    room2 = copy.deepcopy(room)
    adj_room = copy.deepcopy(room)
    visited[s_num] = True

    # 좋아하는 학생이 벌써 앉아있는지 확인
    for i in range(4):
        f_num = friends[i]
        if visited[f_num]:
            already_seat.append(f_num)

    # adj_room -> 인접한 칸 중 비어있는 칸이 얼마나 있는지
    adj_empty = 0
    for x in range(N):
        for y in range(N):
            for d in direction:
                nx, ny = x + d[0], y + d[1]

                if OOB(nx, ny) or room2[nx][ny] < 0 or room2[x][y] < 0:
                    continue

                adj_room[x][y] += 1
                adj_empty = max(adj_empty, adj_room[x][y])

    # 인접한 칸 중 좋아하는 학생이 얼마나 앉아있는지
    temp = [] # 1번 조건 후보군 추출
    adj_fav = 0
    if already_seat: # 좋아하는 학생이 교실에 앉아있는 경우
        for n in already_seat:
            for d in direction:
                nx, ny = dict[n][0]+d[0], dict[n][1]+d[1]

                if OOB(nx, ny) or room2[nx][ny] < 0:
                    continue

                room2[nx][ny] += 1
                adj_fav = max(adj_fav, room2[nx][ny])

        for x in range(N):
            for y in range(N):
                if room2[x][y] == adj_fav and room[x][y] >= 0:
                    temp.append((x, y))

    else: # 좋아하는 학생이 앉아있지 않으면 비어있는 칸이 가장 많은 칸으로 자리 정함
        for x in range(N):
            for y in range(N):
                if adj_room[x][y] == adj_empty:
                    room[x][y] = -s_num
                    dict[s_num] = (x, y)
                    return

    if len(temp) == 1:
        x, y = temp[0][0], temp[0][1]
        room[x][y] = -s_num
        dict[s_num] = (x, y)
        return
    else:
        value = 0
        for t in temp:
            value = max(value, adj_room[t[0]][t[1]])

        for t in temp:
            x, y = t[0], t[1]
            if adj_room[x][y] == value:
                room[x][y] = -s_num
                dict[s_num] = (x, y)
                return

def get_score():
    global score

    for x in range(N):
        for y in range(N):
            cnt = 0
            f_num = -room[x][y]
            for d in direction:
                nx, ny = x + d[0], y + d[1]

                if OOB(nx, ny):
                    continue

                if -room[nx][ny] in fav_dict[f_num]:
                    cnt += 1

            if cnt >0:
                score += 10**(cnt-1)

N = int(input())
s_cnt = N*N
room = [[0] * N for _ in range(N)]
dict = defaultdict()
fav_dict = defaultdict(list)
direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
visited = [False] * (s_cnt+1)
score = 0

for i in range(s_cnt):
    s_num, f1, f2, f3, f4 = map(int, input().split())
    fav_dict[s_num] = [f1, f2, f3, f4]
    assign_seat(s_num, [f1, f2, f3, f4])

get_score()
print(score)