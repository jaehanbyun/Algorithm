import sys

input = sys.stdin.readline

def solution(n: int):
    numbers = []

    for _ in range(n):
        number = input().rstrip()
        numbers.append(number)

    numbers.sort()

    for i in range(n-1):
        if numbers[i] == numbers[i+1][:len(numbers[i])]:
            print("NO")
            break
    else:
        print("YES")

t = int(input())

for _ in range(t):
    n = int(input())
    solution(n)