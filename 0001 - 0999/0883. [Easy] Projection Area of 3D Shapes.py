# https://leetcode.com/problems/projection-area-of-3d-shapes/

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        ans = 0 
        
        for row in grid:
            ans += max(row)
            
        grid = [[grid[i][j] for i in range(n)] for j in range(n)]
        
        for row in grid:
            ans += max(row)
            
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    ans += 1
                    
        return ans
        
                
