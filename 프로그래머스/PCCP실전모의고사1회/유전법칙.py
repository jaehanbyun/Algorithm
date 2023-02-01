L = []
def recursion(n, p):
    if n == 1:
        return
    else:
        n -= 1
        p = p // 4
        L.insert(0, [n, p])
        recursion(n, p)

def solution(queries):
    global L
    answer = []

    for n, p in queries:
        L = []
        p -= 1
        recursion(n, p)
        L.append([n, p])
        P = ["Rr"]
        check = False
        for item in range(1, len(L)):
            if P[-1] == "RR":
                answer.append("RR")
                check = True
                break
            elif P[-1] == "rr":
                answer.append("rr")
                check = True
                break
            else:
                num = (L[item][1]-((L[item][0]-1)*4))%4
                if num == 0:
                    P.append("RR")
                elif num == 1 or num == 2:
                    P.append("Rr")
                elif num == 3:
                    P.append("rr")
        if check == True:
            continue
        else:
            answer.append(P[-1])
    return answer

print(solution([[3, 5]]))