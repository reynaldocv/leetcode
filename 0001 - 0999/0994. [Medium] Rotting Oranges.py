# https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        stack = [(i, j, 2) for j in range(m) for i in range(n) if grid[i][j] == 2]
        seen = {(r, s): True for (r, s, val) in stack}
        ans = 2
        while stack: 
            (x, y, val) = stack.pop(0)
            ans = val
            for (i, j) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                r = x + i
                s = y + j
                if 0 <= r < n and 0 <= s < m: 
                    if grid[r][s] == 1 and (r, s) not in seen: 
                        seen[(r, s)] = True
                        grid[r][s] = val + 1
                        stack.append((r, s, val + 1))
                        
        if sum([1 for j in range(m) for i in range(n) if grid[i][j] == 1]) > 0: 
            return -1
        else: 
            return ans - 2
            
            
            
        
        
