# https://leetcode.com/problems/minimum-path-cost-in-a-grid/

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:        
        m, n = len(grid), len(grid[0])
        
        dp = [grid[0]] + [[inf for _ in range(n)] for _ in range(m - 1)]
              
        for i in range(1, m):
            for j in range(n):
                for k in range(n):
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + moveCost[grid[i - 1][k]][j] + grid[i][j])
        
        return min(dp[-1])
        
class Solution2:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        @cache 
        def helper(x, y):
            if x == m - 1: 
                return grid[x][y]
            
            else: 
                ans = inf 
                
                for q in range(n):
                    ans = min(ans, grid[x][y] + moveCost[grid[x][y]][q] + helper(x + 1, q))
                    
                return ans 
                
        m, n = len(grid), len(grid[0])
        
        return min(helper(0, y) for y in range(n))
        
