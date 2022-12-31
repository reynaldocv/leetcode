# https://leetcode.com/problems/unique-paths-iii/

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def helper(x, y, seen):
            nonlocal ans
            
            for (r, s) in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                p, q = x + r, y + s
                
                if 0 <= p < m and 0 <= q < n and (p, q) not in seen:
                    if grid[p][q] == 2:
                        if len(seen) == length: 
                            ans += 1 
                            
                    elif grid[p][q] == 0: 
                        helper(p, q, seen | set([(x, y)]))
        
        m, n = len(grid), len(grid[0])
        
        length = m*n - 2
        
        start = None
        
        for x in range(m):
            for y in range(n):
                if grid[x][y] == -1:
                    length -= 1
                    
                if grid[x][y] == 1:
                    start = (x, y)
                    
        ans = 0 
        
        helper(start[0], start[1], set())
        
        return ans
