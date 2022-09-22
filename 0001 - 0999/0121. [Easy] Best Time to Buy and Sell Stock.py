# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        suffix = [price for price in prices]
        
        for i in range(n - 2, -1, -1):
            suffix[i] = max(suffix[i], suffix[i + 1])
            
        ans = 0 
        
        for i in range(n - 1):
            ans = max(ans, suffix[i + 1] - prices[i])
            
        return ans 
        
