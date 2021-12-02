# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def markIsland(grid, x, y, n, m, val):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            points = [(x, y)]
            while len(points) > 0:                
                (x, y) = points.pop()
                grid[x][y] = val
                for (i, j) in directions: 
                    r, s = x + i, y + j
                    if 0 <= r < n and 0 <= s < m:                        
                        if grid[r][s] == "*":
                            points.append((r, s))
                            
        n, m = len(grid), len(grid[0])
        grid = [["*" if grid[i][j] == "1" else "0" for j in range(m)] for i in range(n)]
      
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "*":
                    ans += 1        
                    markIsland(grid, i, j, n, m, ans)
                    
        return ans 
