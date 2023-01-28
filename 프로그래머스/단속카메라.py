def solution(routes):
    answer = 0
    car = [0] * len(routes)
    sortroutes = sorted(routes, key=lambda x: x[1])
    print(sortroutes)

    for i in range(len(sortroutes)):
        if car[i] == 0:
            num = sortroutes[i][1]
            num2 = -30000
            k = i
            while num >= num2:
                car[k] = 1
                k += 1
                if k == len(sortroutes):
                    break
                if car[k] == 0:
                    num2 = sortroutes[k][0]
            answer += 1

    return answer