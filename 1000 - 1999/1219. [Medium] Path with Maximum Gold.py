# https://leetcode.com/problems/path-with-maximum-gold/

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def helper(x, y):
            ans = 0 
            val = grid[x][y]
            for (r, s) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                p, q = x + r, y + s
                if 0 <= p < m and 0 <= q < n: 
                    if (p, q) not in seen and grid[p][q] > 0: 
                        seen[(p, q)] = True
                        ans = max(ans, helper(p, q))
                        seen.pop((p, q))
                        
            return val + ans
            
        m, n = len(grid), len(grid[0])
        
        ans = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0: 
                    seen = {(i, j): True}
                    ans = max(ans, helper(i, j))
                
        return ans
        
        
