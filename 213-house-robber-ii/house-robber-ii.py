class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        N = len(nums)
        def fn(i, n, dp):
            if i >= n + 1:
                return 0
            if i in dp:
                return dp[i]

            pick = nums[i] + fn(i + 2, n, dp)
            not_pick = 0 + fn(i + 1, n, dp)

            dp[i] = max(pick, not_pick)
            
            return dp[i]

        return max(fn(0, N - 2, {}), fn(1, N - 1, {}))
        