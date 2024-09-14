def solution(s):
    answer = len(s)

    def get_slice_len(unit):
        nonlocal s

        new_s = []
        for i in range(0, len(s), unit):
            if i + unit > len(s):
                new_s.append(s[i:])
            else:
                new_s.append(s[i:i + unit])

        dp = [0 for _ in range(len(new_s))]
        dp[0] = 1

        for i in range(1, len(new_s)):
            if new_s[i - 1] == new_s[i]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 1

        f_s = new_s[0]
        flag = False
        for i in range(1, len(new_s)):
            if dp[i] == 1:
                if dp[i - 1] != 1:
                    f_s += str(dp[i - 1])
                f_s += new_s[i]

        if dp[-1] != 1:
            f_s += str(dp[-1])

        return len(f_s)

    for u in range(1, len(s) + 1):
        answer = min(answer, get_slice_len(u))

    return answer