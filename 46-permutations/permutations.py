class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # For permuations it's an n! time complexity or operation.

        # We use the 3ps forumula i.e. push(not seen number) path pop

        res, sol = [], []

        def backtrack():
            # base case.
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            
            for num in nums:
                if num not in sol:
                    sol.append(num)
                    backtrack()
                    sol.pop()

        backtrack()
        return res
