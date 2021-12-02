# https://leetcode.com/problems/cyclically-rotating-a-grid/

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        r1, r2, c1, c2 = 0, n - 1, 0, m - 1
        
        while r1 < r2 and c1 < c2: 
            values = []
            for i in range(c1, c2):
                values.append(grid[r1][i])
                
            for j in range(r1, r2):
                values.append(grid[j][c2])
                
            for i in range(c2, c1, -1):
                values.append(grid[r2][i])                
            
            for j in range(r2, r1, -1):
                values.append(grid[j][c1])
                
            rot = k % (len(values))
            values = values[rot:] + values[:rot]
            
            idx = 0
            for i in range(c1, c2):
                grid[r1][i] = values[idx]
                idx += 1
                
            for j in range(r1, r2):
                grid[j][c2] = values[idx]
                idx += 1
                
            for i in range(c2, c1, -1):
                grid[r2][i] = values[idx]
                idx += 1
            
            for j in range(r2, r1, -1):
                grid[j][c1] = values[idx]
                idx += 1
                
            r1, r2, c1, c2 = r1 + 1, r2 - 1, c1 + 1, c2 - 1
            
        return grid
            
            
        
