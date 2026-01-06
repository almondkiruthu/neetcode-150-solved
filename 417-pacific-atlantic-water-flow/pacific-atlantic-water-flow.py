from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # pacific ocean structures.
        p_q = deque()
        p_set = set()

        # Atlantic ocean structures.
        a_q = deque()
        a_set = set()

        rows = len(heights)
        cols = len(heights[0])

        # Get all the coordinates next to the oceans.
        # Vertical borders (Left = Pacific, Right = Atlantic)
        for r in range(rows):
            # Left border (Pacific)
            p_set.add((r, 0))
            p_q.append((r, 0))
            
            # Right border (Atlantic)
            a_set.add((r, cols - 1))
            a_q.append((r, cols - 1))
            
        # Horizontal borders (Top = Pacific, Bottom = Atlantic)
        for c in range(cols):
            # Top border (Pacific)
            p_set.add((0, c))
            p_q.append((0, c))
            
            # Bottom border (Atlantic)
            a_set.add((rows - 1, c))
            a_q.append((rows - 1, c))

        def get_coords(queue, seen):
            # Perform the BFS on each position so far.
            while queue:
                n = len(queue)
                for _ in range(n):
                    i, j = queue.popleft()
                    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                    for dr, dc in directions:
                        n_r = dr + i
                        n_c = dc + j
                        # what's the unwanted case?
                        if (n_r < 0 or n_r >= rows or
                            n_c < 0 or n_c >= cols or
                            # We are going upstream therefore neighbor must be of greater
                            # height than what we have currently.
                            heights[n_r][n_c] < heights[i][j] or
                            (n_r, n_c) in seen):
                            continue
                        else:
                            queue.append((n_r, n_c))
                            seen.add((n_r, n_c))

        get_coords(p_q, p_set)
        get_coords(a_q, a_set)

        return list(p_set.intersection(a_set))

        