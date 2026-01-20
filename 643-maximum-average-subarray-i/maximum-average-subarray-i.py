class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_start = 0
        window_end = 0
        max_sum = float("-inf")

        window_sum = 0
        while window_end < len(nums):
            # Let's continue expand our window.
            window_sum += nums[window_end]

            # But if the window size is greater than the give variable.
            # Let's always shrink.
            if window_end - window_start + 1 == k:
                max_sum = max(max_sum, window_sum / k)
                window_sum -= nums[window_start]
                window_start += 1
            
            window_end += 1
        
        return max_sum