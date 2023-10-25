T = int(input())

for i in range(T):
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    partAnswer = 0

    for i in range(2, N):
        partAnswer = max(partAnswer, abs(arr[i] - arr[i - 2]))

    print(partAnswer)