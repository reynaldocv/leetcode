# https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/

class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:        
        def helper(number):
            cnt2 = 0 
            cnt5 = 0 
            
            while number % 2 == 0: 
                cnt2 += 1 
                
                number //= 2 
                
            while number % 5 == 0: 
                cnt5 += 1 
                
                number //= 5
                
            return [cnt2, cnt5]
        
        m, n = len(grid), len(grid[0])
        
        dp = [[helper(grid[i][j]) for j in range(n)] for i in range(m)]
        
        horizontal = [[[num for num in dp[i][j]] for j in range(n)] for i in range(m)]
        vertical = [[[num for num in dp[i][j]] for j in range(n)] for i in range(m)]
        
        for i in range(m):
            for j in range(1, n):
                horizontal[i][j][0] += horizontal[i][j - 1][0]
                horizontal[i][j][1] += horizontal[i][j - 1][1]
                
        for i in range(1, m):
            for j in range(n):
                vertical[i][j][0] += vertical[i - 1][j][0]
                vertical[i][j][1] += vertical[i - 1][j][1]
                
        ans = 0 
                   
        for i in range(m):
            for j in range(n):
                up2 = vertical[i][j][0]
                up5 = vertical[i][j][1]
                
                down2 = vertical[-1][j][0] - up2 + dp[i][j][0]
                down5 = vertical[-1][j][1] - up5 + dp[i][j][1]
                
                left2 = horizontal[i][j][0] - dp[i][j][0]
                left5 = horizontal[i][j][1] - dp[i][j][1]
                
                right2 = horizontal[i][-1][0] - horizontal[i][j][0]
                right5 = horizontal[i][-1][1] - horizontal[i][j][1]
                
                ans = max(ans, min(up2 + left2, up5 + left5))
                ans = max(ans, min(up2 + right2, up5 + right5))
                ans = max(ans, min(down2 + left2, down5 + left5))
                ans = max(ans, min(down2 + right2, down5 + right5))    
                
        return ans 
                
                
        
        
        
