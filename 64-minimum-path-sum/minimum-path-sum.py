class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = {}

        # tabulation
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[(0, 0)] = grid[i][j]
                    continue

                # do stuffs on the index.
                # invert bottom -> up and right -> left
                up = float("inf")
                left = float("inf")
                if i - 1 >= 0:
                    up = grid[i][j] + dp[(i - 1, j)]
                if j - 1 >= 0:
                    left = grid[i][j] + dp[(i, j - 1)]

                dp[(i, j)] = min(up, left)

        return dp[(m - 1, n - 1)]