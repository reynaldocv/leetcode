# https://leetcode.com/problems/shift-2d-grid/

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        aux = []
        n = len(grid)
        m = len(grid[0])
        q = n*m
        for i in range(n):
            for j in range(m):
                aux.append(grid[i][j])
                
        for i in range(n):
            for j in range(m):
                pos = i*m + j
                grid[i][j] = aux[(pos - k + q) % q]
        
        return grid
        
