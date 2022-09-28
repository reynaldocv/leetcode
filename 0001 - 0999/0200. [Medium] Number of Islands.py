# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def helper(x, y):
            stack = [(x, y)]
            grid[x][y] = "0"
            
            while stack: 
                (x, y) = stack.pop() 
                
                for (r, s) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    p, q = x + r, y + s
                    
                    if 0 <= p < m and 0 <= q < n and grid[p][q] == "1":
                        grid[p][q] = "0"
                        stack.append((p, q))
                            
            return 1 
        
        m, n = len(grid), len(grid[0])
        
        ans = 0 
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans += helper(i, j)
                    
        return ans 
