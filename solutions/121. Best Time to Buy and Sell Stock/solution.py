class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        minSoFar = prices[0]
        maxProfit = prices[1] - prices[0]
        for price in prices:
            minSoFar = min(minSoFar, price)
            maxProfit = max(maxProfit, price - minSoFar)
        return maxProfit