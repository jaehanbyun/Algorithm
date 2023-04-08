import sys

num = int(sys.stdin.readline())
table = [[] for i in range(num+1)]
cost = [0]*(num+1)

for i in range(1, num+1):
    job = []
    end, eachcost = map(int, sys.stdin.readline().split())
    end += i - 1
    if end < num+1:
        job.extend([i, end, eachcost])
        table[end].append(job)

for i in range(1, num+1):
    if len(table[i])!=0:
        tmp = 0
        for start, end, eachcost in table[i]:
            if cost[start-1]+eachcost > tmp:
                tmp = cost[start-1] + eachcost
        if tmp > cost[i-1]:
            cost[i] = tmp
        else:
            cost[i] = cost[i-1]
    else:
        cost[i] = cost[i-1]


print(cost[-1])