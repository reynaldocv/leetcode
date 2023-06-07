# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def helper(x, y):
            stack = [(x, y)]
            
            ans = grid[x][y]
            
            grid[x][y] = 0
            
            while stack: 
                (x, y) = stack.pop() 
                
                for (r, s) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    p, q = x + r, y + s
                    
                    if 0 <= p < m and 0 <= q < n and grid[p][q] > 0: 
                        ans += grid[p][q]
                        
                        grid[p][q] = 0 
                        
                        stack.append((p, q))
                        
            return ans 
        
        m, n = len(grid), len(grid[0])
        
        ans = 0 
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0: 
                    ans = max(ans, helper(i, j))
                    
        return ans 
