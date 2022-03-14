# https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        nextCell = {}
        nextCell[1] = [(0, 1), (0, -1)]
        nextCell[2] = [(1, 0), (-1, 0)]
        nextCell[3] = [(1, 0), (0, -1)]
        nextCell[4] = [(0, 1), (1, 0)]
        nextCell[5] = [(0, -1), (-1, 0)]
        nextCell[6] = [(-1, 0), (0, 1)]
        
        m, n = len(grid), len(grid[0])
        
        stack = [(0, 0)]
        seen = {(0, 0): True}
        
        while stack:
            (x, y) = stack.pop()
            if x == m - 1 and y == n - 1: 
                return True 
            
            for (r, s) in nextCell[grid[x][y]]:
                p, q = x + r, y + s
                if 0 <= p < m and 0 <= q < n:                     
                    if (p, q) not in seen: 
                        if (-r, -s) in nextCell[grid[p][q]]:
                            seen[(p, q)] = True 
                            stack.append((p, q))

        return False
