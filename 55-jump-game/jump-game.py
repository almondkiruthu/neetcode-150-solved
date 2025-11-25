class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index_can_be_reached = 0

        for i in range(len(nums)):
            # These are the max jumps I can do from where I am.
            max_steps = nums[i] + i

            # But if your current index is greater than what we can possibly reach
            # then this can't be true return false.
            if i > max_index_can_be_reached:
                return False

            max_index_can_be_reached = max(max_index_can_be_reached, max_steps)
        return True