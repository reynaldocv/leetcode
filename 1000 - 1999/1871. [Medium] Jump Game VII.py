# https://leetcode.com/problems/jump-game-vii/

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == "1": 
            return False 
        
        n = len(s)
        dp = [False for _ in range(n)]
        
        dp[-1] = True 
        
        tc = 0 
        for i in range(n - 2, -1, -1):
            if i + 1 + maxJump < n and dp[i + 1 + maxJump] == True: 
                tc -= 1
            if i + minJump < n and dp[i + minJump] == True: 
                tc += 1
                
            if s[i] == "1": 
                continue 
            
            dp[i] = tc >= 1  

        return dp[0]
        
