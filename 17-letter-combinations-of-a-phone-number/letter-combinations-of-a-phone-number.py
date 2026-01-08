class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ans, sol = [], []

        def dfs(i):
            if i == len(digits):
                ans.append("".join(sol[:]))
                return
            digit = digits[i]
            letters = phone[digit]

            for char in letters:
               # not here we only include one char pressing a phone number indicates 
               # either of the characters.
               # Push Path Pop
               sol.append(char)
               dfs(i + 1)
               sol.pop()
            
        dfs(0)
        return ans