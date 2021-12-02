# https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:        
        numCoins = [inf]*(amount + 1)     
        numCoins[0] = 0
        for i in range(amount + 1):
            for coin in coins: 
                if i + coin <= amount: 
                    numCoins[i + coin] = min(numCoins[i + coin], numCoins[i] + 1)
        
        return -1 if numCoins[amount] == inf else numCoins[amount]
       
            
