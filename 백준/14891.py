import sys

wheel = []

for _ in range(4):
    wheel.append(list(map(int, sys.stdin.readline().strip('\n'))))

num = int(sys.stdin.readline())

def rotate_wheel(unit, d):
    afterunit = []
    if d == 1:
        tmp = unit[-1]
        afterunit.append(tmp)
        afterunit.extend(unit[0:7])
    else:
        tmp = unit[0]
        afterunit.extend(unit[1:])
        afterunit.append(tmp)
    return afterunit

def check_right(index, d):
    if index == 4 or wheel[index-1][2] == wheel[index][6]:
        return
    else:
        check_right(index+1, -d)
        wheel[index] = rotate_wheel(wheel[index], d)


def check_left(index, d):
    if index == -1 or wheel[index][2] == wheel[index+1][6]:
        return
    else:
        check_left(index-1, -d)
        wheel[index] = rotate_wheel(wheel[index], d)

for i in range(num):
    target, d = map(int, sys.stdin.readline().split())
    target -= 1
    check_right(target+1, -d)
    check_left(target-1, -d)
    wheel[target] = rotate_wheel(wheel[target], d)

score = 0

for i in range(4):
    if wheel[i][0] == 1:
        score += 2**i

print(score)