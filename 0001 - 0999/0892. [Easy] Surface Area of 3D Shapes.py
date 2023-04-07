# https://leetcode.com/problems/surface-area-of-3d-shapes/

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        def helper(arr):
            ans = 0 
            
            last = 0 
            
            for num in arr + [0]:
                ans += abs(num - last)
                
                last = num
                
            return ans 
        
        n = len(grid)
        
        ans = 0 
        
        for row in grid: 
            ans += helper(row)
            
        grid = [[grid[j][i] for j in range(n)] for i in range(n)]
        
        for row in grid: 
            ans += helper(row)
            
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0: 
                    ans += 2 
                    
        return ans 
    
