# https://leetcode.com/problems/island-perimeter/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def helper(arr):
            prev = 0 
            ans = 0 
            
            for num in arr + [0]:
                if num == 0: 
                    if prev == 1: 
                        ans += 1 
                        
                prev = num 
                    
            return ans 
        
        m, n = len(grid), len(grid[0])
        
        ans = 0 
        
        for row in grid: 
            ans +=  2*helper(row)
            
        grid = [[grid[i][j] for i in range(m)] for j in range(n)]
        
        for row in grid: 
            ans += 2*helper(row)
            
        return ans 
        
        
