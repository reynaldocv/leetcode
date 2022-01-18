# https://leetcode.com/problems/stone-game-iv/

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False for _ in range(n + 1)]
              
        for i in range(1, n + 1):
            limit = int(i**.5)
            
            for j in range(1, limit + 1):                
                if dp[i - j**2] == False:
                    dp[i] = True
                    break
                    
        return dp[-1]

class Solution2:
    def winnerSquareGame(self, n: int) -> bool:
        @cache
        def helper(n):
            if n == 0: 
                return False
            else: 
                ans = False
                limit = int(n**.5)
                
                for i in range(1, limit + 1):
                    if not helper(n - i**2):
                        ans = True
                        break
                        
                return ans
                    
        return helper(n)
