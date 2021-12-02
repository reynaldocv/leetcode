# https://leetcode.com/problems/coin-change-2/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def ways(amount, maxCoin):
            if amount == 0: 
                return 1
            elif (amount, maxCoin) in seen: 
                return seen[(amount, maxCoin)]
            else: 
                ans = 0 
                for coin in coins: 
                    if coin <= maxCoin and amount - coin >= 0: 
                        ans += ways(amount - coin, coin)
                seen[(amount, maxCoin)] = ans
                return ans
            
        seen = {(0, 0): 1}
        return ways(amount, max(coins))
    
class Solution2:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount + 1)
        dp[0] = 1
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        
        return dp[-1]
                
        
        
