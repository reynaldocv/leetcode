# https://leetcode.com/problems/largest-magic-square/

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        dp = [[(0, 0, 0, 0) for _ in range(n + 1)] for _ in range(m + 1)] 
        
        for i in range(1, m + 1):                        
            for j in range(1, n + 1):
                dp[i][j] = [
                    dp[i][j - 1][0] + grid[i - 1][j - 1], 
                    dp[i - 1][j][1] + grid[i - 1][j - 1],
                    dp[i - 1][j - 1][2] + grid[i - 1][j - 1],
                    (dp[i - 1][j + 1][3] if j < n else 0) + grid[i - 1][j - 1],
                ]
                
        for ans in range(min(m, n), 0, -1):                 
            for i in range(ans, m + 1):                       
                for j in range(ans, n + 1):                   
                    val = dp[i][j][2] - dp[i - ans][j - ans][2] 
                    if dp[i][j - ans + 1][3] - (dp[i - ans][j + 1][3] if j + 1 <= n else 0) != val: 
                        continue           
                    if any(dp[row][j][0] - dp[row][j - ans][0] != val for row in range(i, i - ans, -1)):
                        continue 
                    if any(dp[i][col][1] - dp[i - ans][col][1] != val for col in range(j, j - ans, -1)):
                        continue 
                        
                    return ans
        return 1
        
        
        
