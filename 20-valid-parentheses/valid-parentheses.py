class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {"}":"{", ")":"(", "]":"["}

        for char in s:
            if char in "{([":
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                # if we haven't returned at this point it means char is a closing
                # bracket.
                if d[char] != stack.pop():
                    return False
        
        return len(stack) == 0