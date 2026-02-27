class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        def traverse(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            
            # Gone over bounds
            if i >= m or j >=n :
                return 0
            # Reached the goal
            if i == m - 1 and j == n - 1:
                return 1
            
            # Go right
            right = traverse(i, j + 1)

            # Go bottom
            bottom = traverse(i + 1, j)

            # return the right and the bottom counts
            dp[(i, j)] = right + bottom

            return dp[(i, j)]

        return traverse(0, 0)
