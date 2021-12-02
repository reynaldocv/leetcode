# https://leetcode.com/problems/detect-cycles-in-2d-grid/

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def helper(x, y):
            val = grid[x][y]
            prev = (-inf, -inf)
            stack = [((x, y), prev)]
            seen = {(x, y): True}
            
            while stack: 
                ((x, y), prev) = stack.pop(0)
                for (r, s) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= r < n and 0 <= s < m: 
                        if (r, s) != prev and grid[r][s] == val: 
                            if (r, s) in seen: 
                                return True
                            else: 
                                seen[(r, s)] = True
                                stack.append(((r, s), (x, y)))

            for (r, s) in seen: 
                grid[r][s] = "$"
                    
            return False 
            
        n, m = len(grid), len(grid[0])
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] != "$":
                    if helper(i, j):
                        return True
                    
        return False
