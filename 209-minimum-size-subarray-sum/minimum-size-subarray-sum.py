class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_start = 0
        window_end = 0
        min_length = float("inf")
        n = len(nums)

        window_sum = 0
        while window_end < n:
            window_sum += nums[window_end]

            while window_sum >= target:
                # I have found my target, can we shrink? And move forward to see
                # If we can find a larger one?
                window_size = window_end - window_start + 1
                min_length = min(min_length, window_size)
                window_sum -= nums[window_start]
                window_start += 1
            
            window_end += 1


        if min_length == float("inf"):
            return 0
        else:
            return min_length
