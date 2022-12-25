# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def helper(i):
            if i >= n: 
                return 0 
            
            else: 
                ans = helper(i + 1)
                
                for j in range(i, n - 1):
                    ans = max(ans, prices[j + 1] - prices[i] + helper(j + 3))
                    
                return ans 
        
        n = len(prices)
        
        return helper(0)

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:

        dp = [0] * len(prices)
        for j in range(len(prices)):
            for i in range(j):
                dp[j] = max(dp[j], (dp[i - 2] if i >= 2 else 0) + prices[j] - prices[i], dp[i])
                
        return dp[-1]
