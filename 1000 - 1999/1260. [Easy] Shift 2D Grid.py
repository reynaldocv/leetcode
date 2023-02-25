# https://leetcode.com/problems/shift-2d-grid/

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        
        ans = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                index = (i*n + j + k) % (m*n)
                
                x = index//n 
                y = index % n
                
                ans[x][y] = grid[i][j]
                
        return ans 
        
