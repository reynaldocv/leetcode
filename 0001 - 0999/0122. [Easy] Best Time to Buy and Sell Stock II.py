# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1: return 0
        ans = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:               
                ans += prices[i] - prices[i - 1]
                
        return ans
