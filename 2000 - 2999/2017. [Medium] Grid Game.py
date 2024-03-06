# https://leetcode.com/problems/grid-game/

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        
        for i in range(1, m):
            grid[0][i] += grid[0][i - 1]

        for i in range(m - 2, -1, -1):
            grid[1][i] += grid[1][i + 1]
            
        ans = inf 
        
        for i in range(m):
            right = grid[0][-1] - grid[0][i]
            left = grid[1][0] - grid[1][i]
            
            ans = min(ans, max(right, left))
            
        return ans 
            
        
        
