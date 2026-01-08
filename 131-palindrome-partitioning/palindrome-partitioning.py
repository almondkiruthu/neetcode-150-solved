class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # consider every single partition of the substring.
        ans, sol = [], []
        n = len(s)

        def dfs(i):
            if i >= n:
                ans.append(sol[:])
                return
            
            # Use the 3 methodology of Push, Path, Pop
            for j in range(i, n):
                sub_string = s[i : j + 1]
                # if our current substring is a substring
                if sub_string == sub_string[::-1]:
                    sol.append(sub_string)
                    dfs(j + 1)
                    # Backtrack
                    sol.pop()

        dfs(0)
        return ans