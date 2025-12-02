class Solution:
    def trap(self, height: List[int]) -> int:
        l_wall = 0
        r_wall = 0
        n = len(height)
        l_max = [0] * n
        r_max = [0] * n

        i = 0
        for i in range(n):
            j = -i - 1
            l_max[i] = l_wall
            r_max[j] = r_wall
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])

        total = 0
        for i in range(n):
            potential_fill = min(l_max[i], r_max[i])
            total += max(0, potential_fill - height[i])

        return total