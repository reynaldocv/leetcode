# https://leetcode.com/problems/right-triangles/

class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        onesRow = [0 for _ in range(m)]
        onesCol = [0 for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                onesRow[i] += grid[i][j]
                onesCol[j] += grid[i][j]
                
        ans = 0 
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: 
                    ans += (onesRow[i] - 1)*(onesCol[j] - 1)
                
        return ans 
    
    
        
