# https://leetcode.com/problems/surface-area-of-3d-shapes/

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        def groupNumberGreaterThanK(array , k):
            n = len(array)
            ans = 0
            if array[0] >= k:
                ans = 1
            for i in range(n - 1):
                if array[i] < k and array[i + 1] >= k: 
                    ans += 1
            return ans
        
        n = len(grid)
        max_ = 0
        ans = 0
        for i in range(n): 
            for j in range(n):
                if grid[i][j] != 0: 
                    ans += 1
                    max_ = max(max_, grid[i][j])
        ans *= 2
       
        
        grid2 = [[grid[i][j] for i in range(n)] for j in range(n)]
        
        for row in grid:
            for k in range(1, max_ + 1):
                ans += 2*groupNumberGreaterThanK(row, k)
                    
        for row in grid2:
            for k in range(1, max_ + 1):
                ans += 2*groupNumberGreaterThanK(row, k)
                
        return ans
    
