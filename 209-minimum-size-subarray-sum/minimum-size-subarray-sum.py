class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        windowSum = 0
        windowStart = 0
        min_length = float("inf")

        for windowEnd in range(len(nums)):
            windowSum += nums[windowEnd]

            while windowSum >= target:
                windowSize = windowEnd - windowStart + 1
                min_length = min(min_length, windowSize)
                windowSum -= nums[windowStart]
                windowStart += 1
        
        # We check if our minimum is still what we started with return zero
        if min_length == float("inf"):
            return 0
        else:
            return min_length
       

        