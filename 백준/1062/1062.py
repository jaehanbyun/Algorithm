import sys
from itertools import combinations
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def countReadableWords(check):
    cnt = 0

    for word in words:
        for c in word:
            if check[ord(c) - 97] == 0:
                break
        else:
            cnt += 1

    return cnt

N, K = map(int, input().split())
base_chars = {'a', 'n', 't', 'i', 'c'}
chars = set(chr(i) for i in range(97, 123)) - base_chars
words = []

for _ in range(N):
    word = input().rstrip()[4:-4]
    words.append(word)

if K < 5:
    print(0)
else:
    rst = 0
    check = [0] * 26

    for w in base_chars:
        check[ord(w) - 97] = 1

    for c_set in combinations(chars, K-5):
        for c in c_set:
            check[ord(c) - 97] = 1

        cnt = countReadableWords(check)
        rst = max(rst, cnt)

        for c in c_set:
            check[ord(c) - 97] = 0

    print(rst)