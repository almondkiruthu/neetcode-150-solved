class Solution:
    def climbStairs(self, n: int) -> int:
        # Tabulation format:
        dp = {}

        # Hardcode your base cases
        dp[n] = 1
        dp[n + 1] = 0
        
        for i in range(n - 1, -1, -1):
            path_1 = dp[i + 1]
            path_2 = dp[i + 2]
            dp[i] = path_1 + path_2

        return dp[0]