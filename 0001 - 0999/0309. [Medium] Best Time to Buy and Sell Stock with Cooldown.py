# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def profit(i):
            if i in seen: 
                return seen[i]
            elif i >= n: 
                return 0 
            else: 
                ans = 0
                for j in range(i + 1, n):
                    ans = max(ans, profit(j))
                
                for j in range(i + 1, n):
                    ans = max(ans, prices[j] - prices[i] + profit(j + 2))
                seen[i] = ans
                return ans
        
        seen = {}
        n = len(prices)
        
        return profit(0)

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:

        dp = [0] * len(prices)
        for j in range(len(prices)):
            for i in range(j):
                dp[j] = max(dp[j], (dp[i - 2] if i >= 2 else 0) + prices[j] - prices[i], dp[i])
                
        return dp[-1]
