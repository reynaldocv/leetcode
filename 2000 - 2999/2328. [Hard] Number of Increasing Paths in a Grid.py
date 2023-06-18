# https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        @cache
        def helper(x, y, prev):            
            if grid[x][y] <=  prev: 
                return 0 
            
            else: 
                ans = 1 
                
                for (r, s) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    p, q = x + r, y + s

                    if 0 <= p < m and 0 <= q < n:
                        ans += helper(p, q, grid[x][y])

                return ans

        MOD = 10**9 + 7
        
        m, n = len(grid), len(grid[0])
        
        ans = 0 
        
        for i in range(m):
            for j in range(n):
                ans += helper(i, j, -1)
                
        return ans % MOD
