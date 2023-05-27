# https://leetcode.com/problems/stone-game-iii/

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @cache
        def helper(i):
            if i == n:
                return 0
            
            ans = stoneValue[i] - helper(i + 1)
            
            if i + 2 <= n:
                ans = max(ans, stoneValue[i] + stoneValue[i + 1] -  helper(i + 2))
            
            if i + 3 <= n:
                ans = max(ans, stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - helper(i + 3))
                
            return ans

        n = len(stoneValue)
        
        dif = helper(0)
        
        if dif > 0:
            return "Alice"
        
        elif dif < 0:
            return "Bob"
        
        return "Tie"
        
