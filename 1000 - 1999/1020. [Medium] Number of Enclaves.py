# https://leetcode.com/problems/number-of-enclaves/

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def helper(x, y):
            stack = [(x, y)]
            
            grid[x][y] = 0 
            seen = {(x, y)}
            
            while stack: 
                (x, y) = stack.pop() 
                
                for (r, s) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    p, q = x + r, y + s
                    
                    if 0 <= p < m and 0 <= q < n: 
                        if grid[p][q] == 1: 
                            grid[p][q] = 0 
                            
                            seen.add((p, q))
                            stack.append((p, q))
                            
            return len(seen)
        
        m, n = len(grid), len(grid[0])
        
        ans = sum(sum(row) for row in grid)
        
        stack = set()
        
        for i in range(m):
            stack.add((i, 0))
            stack.add((i, n - 1))
            
        for j in range(n):
            stack.add((0, j))
            stack.add((m - 1, j))
            
        for (x, y) in stack: 
            if grid[x][y] == 1: 
                ans -= helper(x, y)
                    
        return ans 
        
        
        
        
        
                
