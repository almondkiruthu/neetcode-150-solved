class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        left = right = 0
        # Define our window l and r the decision window/range 
        # each value can make/step/jump
        farthest = 0

        # repeat until right reaches our last elment
        while right < n - 1:
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
            left = right + 1
            right = farthest

            res += 1

        return res
