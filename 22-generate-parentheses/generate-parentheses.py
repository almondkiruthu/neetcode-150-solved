class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, sol = [], []

        def backtrack(open, close):
            if len(sol) == 2 * n:
                ans.append("".join(sol[:]))
                return

            if open < n:
                # we can always open.
                # Push Path pop
                sol.append("(")
                # Path
                backtrack(open + 1, close)
                # Pop undo the changes
                sol.pop()

            if open > close:
                # we can always close
                # Push Path Pop
                sol.append(")")
                # Path
                backtrack(open, close + 1)
                # Pop - undo the changes
                sol.pop()

        backtrack(0, 0)
        return ans