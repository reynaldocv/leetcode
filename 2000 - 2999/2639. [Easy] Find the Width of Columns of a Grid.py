# https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/

class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        def helper(arr):
            ans = 0 
            
            for num in arr:
                ans = max(ans, len(str(num)))
                
            return ans 
        
        ans = []
        
        m, n = len(grid), len(grid[0])
        
        grid = [[grid[i][j] for i in range(m)] for j in range(n)]
        
        for row in grid: 
            ans.append(helper(row))
            
        return ans 
        
        
