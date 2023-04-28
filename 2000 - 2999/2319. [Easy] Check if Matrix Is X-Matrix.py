# https://leetcode.com/problems/check-if-matrix-is-x-matrix/

class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        
        totalSum = sum([sum(row) for row in grid])
        
        aSum = 0 
        
        for i in range(n):
            if grid[i][i] == 0 or grid[i][n - 1 - i] == 0: 
                return False 
            
            aSum += grid[i][i] + grid[i][n - 1 - i]
            
        if n % 2 == 1: 
            aSum -= grid[n//2][n//2]
            
        return totalSum == aSum
            
