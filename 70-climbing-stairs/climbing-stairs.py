class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def fn(i, n):
            # represent in terms of index
            if i == n:
                return 1
            if i > n:
                return 0
            if i in dp:
                return dp[i]
            # on this index I can do 2 things 1 step or 2 step
            # do stuffs on that index
            path_1 = fn(i + 1, n)
            path_2 = fn(i + 2, n)
            # return the sum of all stuffs
            dp[i] = path_1 + path_2
            return dp[i]
        return fn(0, n)