# https://leetcode.com/problems/cherry-pickup/

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        @cache
        def helper(x0, y0, x1, y1):
            if x0 == n - 1 and y0 == n - 1 and x1 == n - 1 and y1 == n  - 1:
                return grid[-1][-1]
            
            else: 
                ans = -inf
                
                for (r0, s0) in [(1, 0), (0, 1)]:
                    for (r1, s1) in [(1, 0), (0, 1)]:
                        p0, q0 = x0 + r0, y0 + s0
                        p1, q1 = x1 + r1, y1 + s1
                        
                        if 0 <= p0 < n and 0 <= q0 < n and 0 <= p1 < n and 0 <= q1 < n:                         
                            if p0 <= p1 and grid[p0][q0] != -1 and grid[p1][q1] != -1:
                                if x0 == x1: 
                                    ans = max(ans, grid[x0][y0] + helper(p0, q0, p1, q1))
                                    
                                else: 
                                    ans = max(ans, grid[x0][y0] + grid[x1][y1] + helper(p0, q0, p1, q1))
                                    
                return ans 
             
        n = len(grid)
        
        if grid[0][0] >= 0:
            stack = [(0, 0)]
            seen = {(0, 0)}
        
        while stack: 
            (x, y) = stack.pop() 
            
            for (r, s) in [(1, 0), (0, 1)]:
                p, q = x + r, y + s
                
                if 0 <= p < n and 0 <= q < n: 
                    if (p, q) not in seen and grid[p][q] != -1: 
                        seen.add((p, q))
                        
                        stack.append((p, q))
                        
        if (n - 1, n - 1) not in seen: 
            return 0 
            
        return helper(0, 0, 0, 0)
    
        
                                    
                                
                            
                        
                        

    
