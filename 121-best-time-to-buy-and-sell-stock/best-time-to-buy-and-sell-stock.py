class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0
        n = len(prices)

        while r < n:
            if prices[l] < prices[r]:
                potential_p = prices[r] - prices[l]
                maxP = max(maxP, potential_p)
            else:
                # if we found a price lower than l then move all the way there.
                l = r
            r += 1

        return maxP