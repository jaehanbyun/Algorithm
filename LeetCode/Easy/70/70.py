class Solution:
    def climbStairs(self, n: int) -> int:
        dp_array = [0 for _ in range(n+1)]
        if n==1:
            return 1

        dp_array[0] = 1
        dp_array[1] = 1

        for i in range(2, n+1):
            dp_array[i] = dp_array[i-1] + dp_array[i-2]

        return dp_array[n]