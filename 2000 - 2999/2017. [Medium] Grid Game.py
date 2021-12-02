# https://leetcode.com/problems/grid-game/

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        for i in range(m - 2, -1, -1):
            grid[0][i] += grid[0][i + 1]
        
        for i in range(1, m):
            grid[1][i] += grid[1][i - 1]
            
        ans = inf
        for i in range(m):
            if i == 0: 
                ans = min(ans, grid[0][1])
            elif i == m - 1:
                ans = min(ans, grid[1][i - 1])
            else: 
                ans = min(ans, max(grid[0][i + 1], grid[1][i - 1]))
            
        return ans
