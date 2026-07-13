class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        N = len(nums)
        def fn(i):
            # we want to reach the last step, so we do inclusive.
            if i >= N:
                return 0
            if i in dp:
                return dp[i]

            reward = float("-inf")
                                    #pick the element       #don't pick
            reward = max(reward, nums[i] + fn(i + 2), 0 + fn(i + 1))
            dp[i] = reward
            return reward
        
        return fn(0)
        
        
