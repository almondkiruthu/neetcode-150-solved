class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # space optimize this:
        prev = [0] * n
        for i in range(m):
            # curr row being processed
            curr = [0] * n
            for j in range(n):
                if i == 0 and j == 0:
                    curr[0] = grid[i][j]
                    continue

                # do stuffs on the index.
                # invert bottom -> up and right -> left
                up = float("inf")
                left = float("inf")
                if i - 1 >= 0:
                    up = grid[i][j] + prev[j]
                if j - 1 >= 0:
                    left = grid[i][j] + curr[j - 1]

                curr[j] = min(up, left)
            
            prev = curr

        return prev[n - 1]