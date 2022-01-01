# https://leetcode.com/problems/coloring-a-border/

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        
        m, n = len(grid), len(grid[0])
        oldColor = grid[row][col]
        
        stack = [(row, col)]    
        seen = {(row, col): True}
        
        while stack: 
            (x, y) = stack.pop()
            for (r, s) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:                
                if (r, s) not in seen: 
                    if 0 <= r < m and 0 <= s < n and grid[r][s] == oldColor:
                        seen[(r, s)] = True
                        stack.append((r, s))
                        
                    else: 
                        grid[x][y] = color
                        
        return grid
                    
