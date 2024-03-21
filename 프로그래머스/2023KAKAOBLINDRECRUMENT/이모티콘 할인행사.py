def solution(users, emoticons):
    def bruteforce(index, l, arr):
        nonlocal total_register, total_money
        if index == l:
            tmp_register, tmp_money = 0, 0
            for dl, rl in users:
                tmp = 0
                for i in range(l):
                    if dl <= arr[i]:
                        tmp += (emoticons[i] * (1 - arr[i] / 100))
                if tmp >= rl:
                    tmp_register += 1
                else:
                    tmp_money += tmp

            if total_register < tmp_register:
                total_register = tmp_register
                total_money = tmp_money
            elif total_register == tmp_register:
                total_money = max(total_money, tmp_money)

            return

        for i in range(4):
            arr.append(discount_rates[i])
            bruteforce(index + 1, l, arr)
            arr.pop()

    total_register, total_money = 0, 0
    each_discount_rate = []
    discount_rates = [10, 20, 30, 40]

    bruteforce(0, len(emoticons), each_discount_rate)

    return [total_register, total_money]