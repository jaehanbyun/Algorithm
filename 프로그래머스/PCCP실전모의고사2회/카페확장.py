from collections import deque
def solution(menu, order, k):
    queue = deque()
    answer = 0
    idx = 0
    comp = -1
    t = [0]*((len(order)-1)*k)

    for o in range(len(t)+1):
        if o == k*idx:
            queue.append(order[idx])
            idx += 1
        if o == comp:
            queue.popleft()
            comp = -1
        if comp == -1 and len(queue) > 0:
            comp = o+menu[queue[0]]

        answer = max(answer, len(queue))

    return answer
