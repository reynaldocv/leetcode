# https://leetcode.com/problems/shortest-bridge/

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        (i, j) = next((i, j) for i in range(n) for j in range(n) if grid[i][j] == 1)
        
        stack = [(i, j)]
        seen = {(i, j)}
       
        while stack: 
            (x, y) = stack.pop() 
            
            for (r, s) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                p, q = x + r, y + s
                
                if 0 <= p < n and 0 <= q < n and grid[p][q] == 1 and (p, q) not in seen: 
                    seen.add((p, q))                    
                    stack.append((p, q))
        
        stack = [(x, y) for (x, y) in seen]
        
        ans = 0
        
        while stack: 
            newStack = []
            
            for (x, y) in stack: 
                for (r, s) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    p, q = x + r, y + s

                    if 0 <= p < n and 0 <= q < n and (p, q) not in seen: 
                        if grid[p][q] == 1: 
                            return ans 
                        
                        seen.add((p, q))

                        newStack.append((p, q))

            stack = newStack
            
            ans += 1 
        
                    

            
