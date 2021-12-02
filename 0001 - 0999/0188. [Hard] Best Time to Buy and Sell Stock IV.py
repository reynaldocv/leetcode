# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k < 1 or len(prices) <= 1:
            return 0

        costs = [prices[0]] + [float('inf')] * (k - 1)
        
        profits = [0] * (k + 1)
      
        for p in range(1, len(prices)):
            for i in range(1, k + 1):
                costs[i - 1] = min(costs[i - 1], prices[p] - profits[i - 1])
                profits[i] = max(profits[i], prices[p] - costs[i - 1])

        return profits[k]
        
