# https://leetcode.com/problems/make-a-square-with-the-same-color/

class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        dp = [[0 for _ in range(4)] for _ in range(4)]
        
        for i in range(1, 4):
            for j in range(1, 4):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
                
                if grid[i - 1][j - 1] == "B":
                    dp[i][j] += 1 
                    
        for i in range(2, 4):            
            for j in range(2, 4):
                cnt = dp[i][j] - dp[i - 2][j] - dp[i][j - 2] + dp[i - 2][j - 2]
                
                if cnt != 2:
                    return True 
                
        return False 
        
        
