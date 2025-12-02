class Solution:
    def isValid(self, s: str) -> bool:
        
        _dict = {"]":"[", "}":"{", ")":"("}

        stack = []
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                # we are still valid to process
                if _dict[char] != stack.pop():
                    return False
        return len(stack) == 0
        