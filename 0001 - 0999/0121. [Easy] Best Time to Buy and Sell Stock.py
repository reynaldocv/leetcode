# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = prices.copy()
        ans, n = 0, len(prices)
        if n <= 1: return 0
        for i in range(n - 2, -1, -1):
            maxP[i] = max(maxP[i], maxP[i + 1])
        
        for i in range(n - 1):
            ans = max(ans, maxP[i + 1] - prices[i])
        
        return ans
        
