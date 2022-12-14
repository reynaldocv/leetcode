# https://leetcode.com/problems/delete-greatest-value-in-each-row/

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        for row in grid: 
            row.sort() 
            
        ans = 0 
        
        for j in range(n):
            tmp = 0
            for i in range(m):
                tmp = max(tmp, grid[i][j])
                
            ans += tmp 
            
        return ans 
                
