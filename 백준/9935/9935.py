import sys

input = sys.stdin.readline

sentence = input().rstrip()
bomb = input().rstrip()

stack = []
b_len = len(bomb)

for i, v in enumerate(sentence):
    stack.append(v)

    if ''.join(stack[-b_len:]) == bomb:
        for _ in range(b_len):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')