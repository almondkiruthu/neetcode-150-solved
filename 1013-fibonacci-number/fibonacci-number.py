class Solution:
    def fib(self, n: int) -> int:
        # Memoization
        # dp = {}
        # def compute_fib(num):
        #     # check base case
        #     if num <= 1:
        #         return num
        #     if num in dp:
        #         return dp[num]
        #     # Save the value if not in dp
        #     dp[num] = compute_fib(num - 1) + compute_fib(num - 2)
        #     # Return that saved value.
        #     return dp[num]
        # return compute_fib(n)

        # # Eliminate recursion calls.
        # dp = [-1] * (n + 1)
        # dp[0] = 0
        # dp[1] = 1

        # for i in range(2, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]

        # return dp[n]

        # Can we actually eliminate space;?
        prev2 = 0
        prev = 1
        res = []
        res.append(prev2)
        res.append(prev)
        if n == 0:
            return 0
        for i in range(2, n + 1):
            curr_i = prev + prev2
            # And let's move our prev2 to be our previous
            prev2 = prev
            # the curr_i will be our new prev
            prev = curr_i
            res.append(prev)

        return prev
    

