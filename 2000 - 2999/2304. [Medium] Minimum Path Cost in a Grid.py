# https://leetcode.com/problems/minimum-path-cost-in-a-grid/

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        @cache
        def helper(i, j):
            if i == m-1: 
                return grid[i][j]
            
            ans = inf 
            for k in range(n): 
                ans = min(ans, grid[i][k] + helper(i + 1, k) + moveCost[grid[i][j]][k])
            
            return ans 
        
        m, n = len(grid), len(grid[0])        
        
        return min(helper(0, j) for j in range(n))
        
