class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        # Go through the tokens, if operand push to stack.

        for token in tokens:
            if token in "+-*/":
                # pop out the last two elements in the stack.
                # first is right-operand and second is left-operand.
                # compute the result and push it to the stack
                if len(stack) >= 2:
                    res = 0
                    right_operand = int(stack.pop())
                    left_operand = int(stack.pop())
                    if token == "+":
                        res = left_operand + right_operand
                    elif token == "-":
                        res = left_operand - right_operand
                    elif token == "*":
                        res = left_operand * right_operand
                    else:
                        res = left_operand / right_operand
                    
                    stack.append(int(res))
            else:
                stack.append(int(token))

        return stack[0]