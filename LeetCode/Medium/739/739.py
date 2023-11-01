class Solution(object):
    def dailyTemperatures(self, temperatures):
        answer = [0] * len(temperatures)
        stack = []

        for cur_day, cur_temp in enumerate(temperatures):
            while stack and stack[-1][1] < cur_temp:
                p = stack.pop()
                answer[p[0]] = cur_day - p[0]
            stack.append((cur_day, cur_temp))

        return answer

sol = Solution()
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))
