class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = {}
        m = len(grid)
        n = len(grid[0])
        def fn(i, j):
            if i == 0 and j == 0:
                return grid[i][j]
            if i < 0 or j < 0:
                return float("inf")
            if (i, j) in dp:
                return dp[(i, j)]
            
            # do stuffs on the index.
            # invert bottom -> up and right -> left
            up = grid[i][j] + fn(i - 1, j)
            left = grid[i][j] + fn(i, j - 1)

            dp[(i, j)] = min(up, left)

            return min(up, left)

        return fn(m - 1, n - 1)