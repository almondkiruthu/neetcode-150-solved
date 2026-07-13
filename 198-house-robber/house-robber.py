class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        N = len(nums)
        # Tabulation we begin from the basecase
        dp[N] = 0
        dp[N + 1] = 0
        dp[N + 2] = 0
        for i in range(N - 1, -1, -1):
            pick = nums[i] + dp[i + 2]
            not_pick = 0 + dp[i + 1]

            dp[i] = max(pick, not_pick)

        return dp[0]
        
        
