# https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        nextRoad = {}
        nextRoad[1] = {(0, -1): {1, 4, 6}, (0, 1): {1, 3, 5}}
        nextRoad[2] = {(-1, 0): {2, 3, 4}, (1, 0): {2, 5, 6}}
        nextRoad[3] = {(1, 0): {2, 5, 6}, (0, -1): {1, 4, 6}}
        nextRoad[4] = {(1, 0): {2, 5, 6}, (0, 1): {1, 3, 5}, }
        nextRoad[5] = {(-1, 0): {2, 3, 4}, (0, -1): {1, 4, 6}}
        nextRoad[6] = {(-1, 0): {2, 3, 4}, (0, 1): {1, 3, 5}}
        
        stack = [(0, 0)]
        seen = {(0, 0)}
        
        while stack:       
            (x, y) = stack.pop() 
            
            if x == m - 1 and y == n - 1: 
                return True 
            
            value = grid[x][y]
            
            for (r, s) in nextRoad[value]:
                p, q = x + r, y + s
                
                if 0 <= p < m and 0 <= q < n: 
                    if (p, q) not in seen: 
                        nextValue = grid[p][q]
                        
                        if nextValue in nextRoad[value][(r, s)]:
                            seen.add((p, q))
                            
                            stack.append((p, q))
                            
        return False 
