# https://leetcode.com/problems/island-perimeter/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def groupOf1(array):
            n = len(array)
            aux, ans = 0, 0
            if array[0] == 1:
                aux, ans = 1, 1
            for i in range(0, n - 1):
                if array[i] == 0 and array[i + 1] == 1:
                    ans += 1
            return ans
        
        row = len(grid)
        col = len(grid[0])        
        grid2 = [[grid[i][j] for i in range(row)] for j in range(col)]
        
        ans = 0
        for i in range(row):
            ans += groupOf1(grid[i])
            
        for i in range(col):
            ans += groupOf1(grid2[i])
                
        return 2*ans
        
        
