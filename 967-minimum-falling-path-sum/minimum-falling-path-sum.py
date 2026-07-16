class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        # Space optimization
        #step 1: represent the base case with a prev_dp
        prev_dp = [0] * n
        for j in range(n):
            prev_dp[j] = matrix[m - 1][j]
        
        for i in range(m - 2, -1, -1):
            # note: if all have the same n.o. of cols but to me more sure, let's use the variable Mth row
            # let's build the cols in reverse as well.
            curr_row = [0] * n
            for j in range(n):
                # do stuffs with the index:
                curr = matrix[i][j]
                bottom = curr + prev_dp[j]
                bottom_left = float("inf")
                if j - 1 >= 0:
                    bottom_left = curr + prev_dp[j - 1]
                bottom_right = float("inf")
                if j + 1 < n:
                    bottom_right = curr + prev_dp[j + 1]
                minima = min(bottom, bottom_right, bottom_left)
                curr_row[j] = minima

            prev_dp = curr_row
        
        res = float("inf")
        for starting_point in range(n):
            res = min(res, prev_dp[starting_point])

        return res