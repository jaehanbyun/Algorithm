import sys

N = int(sys.stdin.readline())
alpha_to_num = {}

for _ in range(N):
    word = sys.stdin.readline().strip()
    word_len = len(word)-1
    for w in word:
        if w in alpha_to_num:
            alpha_to_num[w] += 10**word_len
        else:
            alpha_to_num[w] = 10**word_len
        word_len -= 1

alpha_to_num = sorted(alpha_to_num.values(), reverse=True)

answer = 0
assign_num = 9

for w in alpha_to_num:
    answer += assign_num*w
    assign_num-=1

print(answer)
