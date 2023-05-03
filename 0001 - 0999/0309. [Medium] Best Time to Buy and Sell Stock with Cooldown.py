# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def helper(i):
            if i >= n: 
                return 0 
            
            else: 
                ans = helper(i + 1)
                
                for j in range(i + 1, n):
                    ans = max(ans, prices[j] - prices[i] + helper(j + 2))
                
                return ans 
            
        n = len(prices)
        
        return helper(0)

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        dp = defaultdict(lambda: 0)
        
        for i in range(1, n):
            tmp = dp[i - 1]
            
            for j in range(i):
                if prices[i] > prices[j]:
                    tmp = max(tmp, prices[i] - prices[j] + dp[j - 2])
                    
            dp[i] = tmp 
            
        return dp[n - 1]
                    
