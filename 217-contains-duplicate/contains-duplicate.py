class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        _dict = {}
        for num in nums:
            if num in _dict:
                _dict[num] += 1
                return True
            else:
                _dict[num] = 1
        return False

        