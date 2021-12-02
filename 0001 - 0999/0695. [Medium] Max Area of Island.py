# https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def markIsland(x, y, val):
            points = [(x, y)]
            ans = 0
            while points: 
                (x, y) = points.pop()  
                if grid[x][y] == 1: 
                    grid[x][y] = val
                    ans += 1
                for (i, j) in directions: 
                    r = x + i
                    s = y + j
                    if 0 <= r < n and 0 <= s < m: 
                        if grid[r][s] == 1:
                            points.append((r, s))
            return ans
        
        n = len(grid)
        m = len(grid[0])
        ans = 0 
        val = 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1: 
                    val += 1
                    ans = max(ans, markIsland(i, j, val))
               
        return ans
                    
