# https://leetcode.com/problems/score-after-flipping-matrix/

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for (i, row) in enumerate(grid):
            if row[0] == 0: 
                grid[i] = [1 - num for num in row]
                
        m, n = len(grid), len(grid[0])
        
        ans = 0 
        
        for j in range(n):
            cnt = 0 
            
            for i in range(m):
                cnt += grid[i][j]
                    
            ans += max(cnt, m - cnt)*2**(n - j - 1)
            
        return ans 
                
        
                
