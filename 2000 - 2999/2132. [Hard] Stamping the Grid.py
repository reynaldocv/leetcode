# https://leetcode.com/problems/stamping-the-grid/

class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])
        
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + grid[i - 1][j - 1]
                
        aSum = [[False for _ in range(n)] for _ in range(m)]
        
        for i in range(m - stampHeight + 1):
            for j in range(n - stampWidth  + 1):
                tmp = dp[i + stampHeight][j  + stampWidth]
                tmp -= dp[i + stampHeight][j]
                tmp -= dp[i][j + stampWidth]                
                tmp += dp[i][j]
                
                aSum[i][j] = tmp == 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: 
                    covered = False 
                    
                    for ii in range(i, max(i - stampHeight, -1), -1):
                        if covered: 
                            break 
                        
                        for jj in range(j, max(j - stampWidth, -1),  -1):                            
                            if aSum[ii][jj]: 
                                for r in range(ii, ii  + stampHeight):
                                    for s in range(jj, jj + stampWidth):
                                        grid[r][s] = 1
                                        
                                covered = True 
                                
                                break 
                                
                    if not covered: 
                        return False 
                    
        return True 
                                
                                
                                
                                
                                
                
        
