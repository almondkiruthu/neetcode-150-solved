class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = {}
        def fn(i):
            min_cost = float('inf')
            if i >= n:
                return 0
            if i in dp:
                return dp[i]

            step_1 = cost[i] + fn(i + 1)
            step_2 = cost[i] + fn(i + 2)

            min_cost = min(min_cost, min(step_1, step_2))
            dp[i] = min_cost
            return dp[i]
        
        return min(fn(0), fn(1))
            

