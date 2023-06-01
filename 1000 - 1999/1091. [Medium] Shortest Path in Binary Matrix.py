# https://leetcode.com/problems/shortest-path-in-binary-matrix/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        if grid[0][0] != 0: 
            return -1 
        
        stack = [(0, 0)]
        seen = {(0, 0)}
        
        ans = 1
        
        while stack: 
            newStack = []
            
            for (x, y) in stack: 
                if x == n - 1 and y == n - 1: 
                    return ans 
                
                for (r, s) in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
                    p, q = x + r, y + s
                    
                    if 0 <= p < n and 0 <= q < n and grid[p][q] == 0 and (p, q) not in seen:
                        seen.add((p, q))
                        
                        newStack.append((p, q))
                        
            stack = newStack            
            ans += 1 
            
        return -1 
        
class Solution2:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        distance = defaultdict(lambda: defaultdict(lambda: inf))
        
        if grid[0][0] == 1: 
            return -1 
        
        distance[0][0] = 1 
        
        stack = [(0, 0)]

        while stack: 
            (x, y) = stack.pop(0) 
            
            for (r, s) in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
                    p, q = x + r, y + s
                    
                    if 0 <= p < n and 0 <= q < n and grid[p][q] == 0:
                        if distance[p][q] > distance[x][y] + 1:
                            distance[p][q] = distance[x][y] + 1
                            
                            stack.append((p, q))
                            
        if distance[n - 1][n - 1] == inf: 
            return -1 
        
        return distance[n - 1][n - 1]
        
        
