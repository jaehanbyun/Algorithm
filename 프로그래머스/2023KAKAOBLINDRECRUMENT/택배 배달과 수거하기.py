def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver_last_home, pickup_last_home = n-1, n-1

    while True:
        for i in range(deliver_last_home, -1, -1):
            if deliveries[i] != 0:
                deliver_last_home = i
                break
            else:
                deliver_last_home -= 1

        for i in range(pickup_last_home, -1, -1):
            if pickups[i] != 0:
                pickup_last_home = i
                break
            else:
                pickup_last_home -= 1

        if deliver_last_home == -1 and pickup_last_home == -1:
            break

        last_home = max(deliver_last_home+1, pickup_last_home+1)
        answer += last_home*2

        remain_deliver_box = cap
        for i in range(deliver_last_home, -1, -1):
            if remain_deliver_box >= deliveries[i]:
                remain_deliver_box -= deliveries[i]
                deliveries[i] = 0
            else:
                deliveries[i] -= remain_deliver_box
                break

        remain_pickup_box = cap
        for i in range(pickup_last_home, -1, -1):
            if remain_pickup_box >= pickups[i]:
                remain_pickup_box -= pickups[i]
                pickups[i] = 0
            else:
                pickups[i] -= remain_pickup_box
                break

    return answer
