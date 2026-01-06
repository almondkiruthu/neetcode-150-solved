from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        empty, fresh, rotten = 0, 1, 2
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        minutes = 0
        # Find the number of fresh oranges and append to queue all the rotten oranges position.
        fresh_num = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == fresh:
                    fresh_num += 1
                elif grid[row][col] == rotten:
                    queue.append((row, col))

        if fresh_num == 0:
            return 0
        
        # We will use a bfs approach to traverse this grid.
        # Since we are desiging our traversal to be optimized for neighbours.
        # We have the queue filled up with all the rotten_oranges positions.
        while queue:
            queue_size = len(queue)
            minutes += 1
            # We have visited the rotten oranges positons this simulates the parallel   operations
            for _ in range(queue_size):
                # visited.
                row, col = queue.popleft()
                directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
                # explore
                for dr, dc in directions:
                    n_row = row + dr
                    n_col = col + dc
                    if (n_row < 0 or n_row >= rows or
                        n_col < 0 or n_col >= cols or
                        grid[n_row][n_col] == rotten or
                        grid[n_row][n_col] == empty):
                        continue
                    else:
                        # It's a fresh orange and we are in bounds.
                        grid[n_row][n_col] = rotten
                        fresh_num -= 1
                        queue.append((n_row, n_col))

        if fresh_num > 0:
            return -1
        else:
            return minutes - 1

