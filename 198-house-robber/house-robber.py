class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        N = len(nums)
        # space optimize:
        prev = 0
        prev2 = 0
        for i in range(N - 1, -1, -1):
            pick = nums[i] + prev2
            not_pick = 0 + prev
            curr = max(pick, not_pick)

            prev2 = prev
            prev = curr

        return prev
        
        
