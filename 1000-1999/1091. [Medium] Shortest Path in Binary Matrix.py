# https://leetcode.com/problems/shortest-path-in-binary-matrix/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        distances = [[inf for _ in range(n)] for _ in range(n)]
        distances[0][0] = 1 if grid[0][0] == 0 else inf
        stack = [(0, 0)] if grid[0][0] == 0 else []
        seen = {(0, 0): True}
        
        while stack: 
            (x, y) = stack.pop(0)
            for (i, j) in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                r, s = x + i, y + j
                if 0 <= r < n and 0 <= s < n: 
                    if (r, s) not in seen and grid[r][s] == 0: 
                        distances[r][s] = min(distances[r][s], 1 + distances[x][y])
                        seen[(r, s)] = True
                        stack.append((r, s))
      
        return - 1 if distances[-1][-1] == inf else distances[-1][-1]
        
        
        
