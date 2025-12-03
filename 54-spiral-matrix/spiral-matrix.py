class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix:
            # 1. Add the first row to result
            result += matrix.pop(0)
            
            # 2. Rotate the remaining matrix Counter-Clockwise
            # zip(*matrix) transposes it
            # [::-1] reverses it (to achieve CCW rotation)
            if matrix:
                matrix = list(zip(*matrix))[::-1]
                
        return result