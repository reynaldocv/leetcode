# https://leetcode.com/problems/path-with-maximum-gold/

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def helper(aSum, x, y):
            nonlocal ans 
            
            ans = max(ans, aSum)
            
            for (r, s) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                p, q = x + r, y + s
                
                if 0 <= p < m and 0 <= q < n: 
                    if grid[p][q] > 0: 
                        tmp = grid[p][q]
                        
                        grid[p][q] = 0 
                        
                        helper(aSum + tmp, p, q)
                        
                        grid[p][q] = tmp 
                        
        m, n = len(grid), len(grid[0])
        
        ans = 0 
        
        for i in range(m):
            for j in range(n):
                helper(0, i, j)
                
        return ans 
        
    
        
