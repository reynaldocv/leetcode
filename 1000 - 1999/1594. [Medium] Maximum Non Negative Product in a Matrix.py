# https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        m, n = len(grid), len(grid[0])
        
        dp = [[[grid[i][j], grid[i][j]] for j in range(n)] for i in range(m)]
        
        for j in range(1, n):
            dp[0][j][0] *= dp[0][j - 1][0]
            dp[0][j][1] *= dp[0][j - 1][1]
              
        for i in range(1, m):
            dp[i][0][0] *= dp[i - 1][0][0]
            dp[i][0][1] *= dp[i - 1][0][1]
            
        for i in range(1, m):
            for j in range(1, n):
                tmp = []
                
                for num in dp[i - 1][j]:
                    tmp.append(num*grid[i][j])
                    
                for num in dp[i][j - 1]:
                    tmp.append(num*grid[i][j])
                    
                tmp.sort() 
                
                minElem = min(tmp)
                maxElem = max(tmp)
                
                dp[i][j] = [minElem, maxElem]
                
        return (dp[-1][-1][1] % MOD) if dp[-1][-1][1] >= 0 else -1
        
        
