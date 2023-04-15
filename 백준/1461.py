import sys

n, m = map(int, input().split())

books = list(map(int, input().split()))

left = []
right = []
for book in books:
    if book >= 0:
        right.append(book)
    else:
        left.append(book)

left.sort()
right.sort()

distance = []
left.sort()
for i in range(len(left) // m):
    distance.append(abs(left[m * i]))
if len(left) % m > 0:
    distance.append(abs(left[(len(left) // m) * m]))

right.sort(reverse=True)
for i in range(len(right) // m):
    distance.append(right[m * i])
if len(right) % m > 0:
    distance.append(right[(len(right) // m) * m])

distance.sort()
result = distance.pop()
result += 2 * sum(distance)
print(result)