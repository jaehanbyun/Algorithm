import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

def solution(x, y, n):
    global count

    if ((x <= r < x+n) and (y <= c < y+n)) == False:
        count += n**2
        return

    if n > 2:
        n //= 2
        solution(x, y, n)
        solution(x, y+n, n)
        solution(x+n, y, n)
        solution(x+n, y+n, n)
    else:
        if x==r and y==c:
            print(count)
        elif x==r and y+1==c:
            print(count+1)
        elif x+1==r and y==c:
            print(count+2)
        elif x+1==r and y+1==c:
            print(count+3)
        exit()

N, r, c = map(int, input().split())

count = 0
solution(0, 0, 2**N)