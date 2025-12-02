class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = temperatures
        n = len(temps)
        # Our steps to achieve a temp rise.
        rises = [0] * n
        stack = []

        for i in range(n):
            # handle the condition for popping,
            # while we have a stack 
            while stack and stack[-1][0] < temps[i]:
                stk_val, stk_idx = stack.pop()
                # Gives us the length between the two temps
                rises[stk_idx] = i - stk_idx
            
            # we append no matter what.
            stack.append((temps[i], i))
        
        return rises
