class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Brute Force consider all possible subarrays starting from i
        # sol = float("-inf")
        # for i in range(len(nums)):
        #     curr_sum = 0
        #     for j in range(i, len(nums)):
        #         curr_sum += nums[j]
        #         sol = max(sol, curr_sum)
        # return sol

        sol = float("-inf")
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]

            sol = max(sol, curr_sum)

            if curr_sum < 0:
                curr_sum = 0

        return sol