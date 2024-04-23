import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
sensors = list(map(int, input().split()))
sensor_dist = []

sensors.sort()

for i in range(n-1):
    dist = sensors[i+1] - sensors[i]
    sensor_dist.append(dist)

sensor_dist.sort()

answer = sum(sensor_dist[:n-k])
print(answer)