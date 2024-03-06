# https://leetcode.com/problems/detect-cycles-in-2d-grid/
class Solution01:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def helper(x, y, pX, pY): 
            for (r, s) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                p, q = x + r, y + s
                
                if 0 <= p < m and 0 <= q < n:
                    if grid[x][y] == grid[p][q]:                                                
                        if (p, q) != (pX, pY): 
                            if (p, q) in visited: 
                                return True 

                            else:
                                visited.add((p, q))

                                if helper(p, q, x, y):
                                    return True 

            return False 
        
        m, n = len(grid), len(grid[0])
        
        visited = set([])
        
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:                     
                    visited.add((i, j))
                    
                    if helper(i, j, -1, -1):
                        return True 
        
        return False 
