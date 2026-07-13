class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # Let's tabulate
        def fn_tabulate(arr):
            if len(arr) == 1:
                return arr[0]
            N = len(arr)
            dp = {}
            dp[N] = 0
            dp[N + 1] = 0                     
            for i in range(N - 1, -1, -1):
                pick = arr[i] + dp[i + 2]
                not_pick = 0 + dp[i + 1]
                dp[i] = max(pick, not_pick)
            
            return dp[0]

        first_pass = fn_tabulate(nums[:-1])
        second_pass = fn_tabulate(nums[1:])

        return max(first_pass, second_pass)
        
        