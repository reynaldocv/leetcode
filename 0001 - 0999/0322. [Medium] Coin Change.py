# https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:        
        dp = [0] + [inf for _ in range(amount)]
        
        for coin in coins: 
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], 1 + dp[i - coin])
          
        return dp[-1] if dp[-1] != inf else -1
        
        
        
