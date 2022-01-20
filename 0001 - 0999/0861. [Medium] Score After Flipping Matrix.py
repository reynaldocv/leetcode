# https://leetcode.com/problems/score-after-flipping-matrix/

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        def helper(row):
            return [1 - bit for bit in row]
        
        def collaborator(row):
            ans = 0 
            for (i, bit) in enumerate(row[::-1]):
                ans += bit*2**i
                
            return ans
        
        m, n = len(grid), len(grid[0])
        
        for (i, row) in enumerate(grid): 
            if row[0] == 0:
                grid[i] = helper(row)
                
        gridT = list(zip(*grid))
        
        for (i, row) in enumerate(gridT):
            if sum(row) < (m + 1)//2:
                gridT[i] = helper(row)
        
        grid = list(zip(*gridT))
        
        ans = 0
        for row in grid: 
            ans += collaborator(row)
            
        return ans
                
        
                
