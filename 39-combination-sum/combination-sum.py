class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []

        # Pass down the current index and curr_sum of the path
        # Use the Push Path Pop Path technique, but this time only include from the right
        # side.
        def backtrack(idx, curr_sum):
            if curr_sum == target:
                res.append(sol[:])
                return
            
            if idx >= len(candidates) or curr_sum > target:
                return
            
            # Push, path, pop simply stands for include that idx over and over again.
            sol.append(candidates[idx])
            backtrack(idx, curr_sum + candidates[idx])
            sol.pop()

            backtrack(idx + 1, curr_sum)

        backtrack(0, 0)
        return res