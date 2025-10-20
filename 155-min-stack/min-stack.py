class MinStack:

    def __init__(self):
        self.stack = []
        # auxiliary stack to keep track of the min elements
        self.min_stack = []
    
    def push(self, val: int) -> None:
        # push to ordinary stack
        self.stack.append(val)

        # check if the current min stack doesn't contain the latest min value. i.e.
        # it's non empty.
        # If it's non-empty take the min value between the val to be inserted. and 
        # the current min value at the top of the min-stack.

        # If it's empty append the value it's our current minimum.
        if len(self.min_stack) != 0:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)
    def pop(self) -> None:
        popped_val = self.stack.pop()
        self.min_stack.pop()


        # if popped_val == self.min_stack[-1]:
        #     self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()