# https://leetcode.com/problems/max-increase-to-keep-city-skyline/

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid) 
        
        maxRows = []
        maxCols = []
        
        for i in range(n):
            maxRow = 0 
            maxCol = 0 
            
            for j in range(n):
                maxRow = max(maxRow, grid[i][j])
                maxCol = max(maxCol, grid[j][i])
            
            maxRows.append(maxRow)
            maxCols.append(maxCol)
            
        ans = 0 
            
        for i in range(n):
            for j in range(n):
                ans += min(maxRows[j], maxCols[i]) - grid[i][j]
                
        return ans 
    
