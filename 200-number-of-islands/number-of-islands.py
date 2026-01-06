class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Find the n.o of islands - flag to increment
        num_of_islands = 0
        # Optimize to avoid revisiting ones.
        visited = set()

        rows = len(grid)
        cols = len(grid[0])

        # DFS function, since we prefer depth to find the maximum n.o. of 1s.

        def dfs(row, col):
            # if we are out of bounds and our current position is not land i.e 1
            # we backtrack return.
            if (row < 0 or row >= rows 
                or col < 0 or col >= cols 
                or grid[row][col] == "0"
                or (row, col) in visited):
                return
            else:
                visited.add((row, col))
                # we recursively explore x-and-y axis from current position.
                # move right, left, up, bottom
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    dfs(new_row, new_col)

        for i in range(rows):
            for j in range(cols):
                # Then let's perform our dfs.
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    num_of_islands += 1

        return num_of_islands

        