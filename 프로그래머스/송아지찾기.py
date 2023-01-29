from collections import deque

def bfs(s, e):
    if s-e>0:
        return s-e
    cnt = (e-s)//5
    s = cnt*5+s
    dq = deque()
    dq.append(s)
    while(dq):
        length = len(dq)
        for i in range(length):
            v = dq.popleft()
            if v == e:
                return cnt
            for nv in[v-1, v+1, v+5]:
                dq.append(nv)
        cnt+=1
    return cnt

def solution(s, e):
    return bfs(s, e)