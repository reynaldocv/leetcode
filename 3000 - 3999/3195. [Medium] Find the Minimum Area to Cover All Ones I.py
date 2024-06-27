# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) 
        
        minX, minY = inf, inf 
        maxX, maxY = -1, -1
        
        ans = 0 
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: 
                    minX = min(minX, i)
                    minY = min(minY, j)
                    
                    maxX = max(maxX, i)
                    maxY = max(maxY, j)
                    
                    ans = (maxY - minY + 1)*(maxX - minX + 1)
                    
        return ans 

        
        
