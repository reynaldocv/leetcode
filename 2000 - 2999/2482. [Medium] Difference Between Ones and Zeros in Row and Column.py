# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        @cache 
        def helper(row):
            ans = 0 
            
            for j in range(n):
                ans += grid[row][j]
                
            return ans 
        
        @cache
        def collaborator(col):
            ans = 0 
            
            for i in range(m):
                ans += grid[i][col]
                
            return ans 
            
        m, n = len(grid), len(grid[0])
        
        ans = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                ans[i][j] = 2*helper(i) + 2*collaborator(j) - n - m
                
        return ans 
        
