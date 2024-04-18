# https://leetcode.com/problems/coloring-a-border/

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        def helper(x, y):
            value = grid[x][y]
            
            stack = [(x, y)]
            seen = {(x, y)}
            
            while stack: 
                (x, y) = stack.pop() 
                
                for (r, s) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    p, q = x + r, y + s
                    
                    if 0 <= p < m and 0 <= q < n: 
                        if (p, q) not in seen and grid[p][q] == value: 
                            seen.add((p, q))
                            
                            stack.append((p, q))
                            
            return seen 
                        
        m, n = len(grid), len(grid[0])
        
        ans = [[grid[i][j] for j in range(n)] for i in range(m)]
        
        cells = helper(row, col)
        
        for (x, y) in cells: 
            colors = {grid[x][y]}
            
            for (r, s) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                p, q = x + r, y + s
                
                if 0 <= p < m and 0 <= q < n: 
                    colors.add(grid[p][q])
                else: 
                    colors.add(-1)
                    
            if len(colors) > 1: 
                ans[x][y] = color
                
        return ans
            
            
            
            
        
