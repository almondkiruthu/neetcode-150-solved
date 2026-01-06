class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Mathematical equivalent of nCr = n!/r!(n - r)!

        res, sol = [], []
        # We use the 4p methodology Push, Path, Pop, Path

        def backtrack(x):
            if len(sol) == k:
                res.append(sol[:])
                return
            
            # Push, Path, Pop i.e include
            sol.append(x)
            backtrack(x - 1)
            sol.pop()

            #Path don't include.
            # However to make sure that the base case works check the nums available
            # And how many are still needed.
            left_numbers = x
            still_needed = k - len(sol)
            if left_numbers > still_needed:
                backtrack(x - 1)
        
        backtrack(n)
        return res
