import math
def solution(fees, records):
    answer = []
    defaultTime, defaultFee, unitTime, unitFee = map(int, fees)
    car = [0 for i in range(10000)]
    incar = [0 for i in range(10000)]
    carlived = [0 for i in range(10000)]

    for i in records:
        item = list(i.split(' '))
        if item[2] == 'IN':
            hour, minute = map(int, item[0].split(':'))
            minute += 60 * hour
            car[int(item[1])] = minute
            incar[int(item[1])] = 1
        elif item[2] == 'OUT':
            hour, minute = map(int, item[0].split(':'))
            minute += 60 * hour
            carlived[int(item[1])] += minute - car[int(item[1])]
            car[int(item[1])] = 0
            incar[int(item[1])] = 0

    for j in range(10000):
        if incar[j] == 1:
            carlived[j] += 1439 - car[j]

    for k in carlived:
        if k > 0:
            carfee = defaultFee + max((math.ceil((k - defaultTime) / unitTime)), 0) * unitFee
            answer.append(carfee)

    return answer