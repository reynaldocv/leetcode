# https://leetcode.com/problems/check-if-grid-satisfies-conditions/

class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        for i in range(n - 1):
            if grid[0][i] == grid[0][i + 1]:
                return False 
            
        grid = [[grid[i][j] for i in range(m)] for j in range(n)]
        
        for row in grid: 
            if min(row) != max(row):
                return False 
            
        return True 
                
