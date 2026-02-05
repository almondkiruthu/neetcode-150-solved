class Solution:
    def fib(self, n: int) -> int:
        dp = {}
        def compute_fib(num):
            # check base case
            if num <= 1:
                return num
            if num in dp:
                return dp[num]
            # Save the value if not in dp
            dp[num] = compute_fib(num - 1) + compute_fib(num - 2)
            # Return that saved value.
            return dp[num]
        return compute_fib(n)
    

