class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        cache = {}

        def move_agent(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            
            if (i == rows - 1) and (j == cols - 1) and obstacleGrid[i][j] != 1:
                return 1

            if i >= rows or j >= cols:
                return 0

            # Check for obstacles:
            if obstacleGrid[i][j] == 1:
                return 0
            
            right = move_agent(i, j + 1)
            bottom = move_agent(i + 1, j)

            cache[(i, j)] = right + bottom

            return cache[(i, j)]

        return move_agent(0, 0)

