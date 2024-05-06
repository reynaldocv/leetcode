# https://leetcode.com/problems/cherry-pickup-ii/

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        @cache
        def helper(lvl, i, j):
            if lvl == m - 1: 
                if i == j: 
                    return grid[lvl][i] 
                
                else: 
                    return grid[lvl][i] + grid[lvl][j]
                
            else: 
                ans = 0
                
                for ii in range(i - 1, i + 2):
                    for jj in range(j - 1, j + 2):
                        if 0 <= ii < n and 0 <= jj < n: 
                            if i < j:                             
                                ans = max(ans, grid[lvl][i] + grid[lvl][j] + helper(lvl + 1, ii, jj))
                            
                            elif i == j: 
                                ans = max(ans, grid[lvl][i] + helper(lvl + 1, ii, jj))
                                
                return ans 
            
        m, n = len(grid), len(grid[0])
        
        return helper(0, 0, n - 1)
                            
