# https://leetcode.com/problems/shortest-path-to-get-all-keys/

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        
        keys = {chr(ord("a") + i): i for i in range(6)}
        locks = {chr(ord("A") + i): i for i in range(6)}
        
        stack = []
        numOfKeys = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@': 
                    stack.append((i, j, 0, 0))
                    
                elif grid[i][j] in keys:  
                    numOfKeys += 1
                    
        visited = set()
        
        while stack:
            newStack = []
            
            for (x, y, found, steps) in stack:
                cur = grid[x][y]
                
                if cur in locks and not (found >> locks[cur]) & 1 or cur == '#':
                    continue
                    
                if cur in keys:  
                    found |= 1 << keys[cur]
                    
                    if found == (1 << numOfKeys) - 1:  
                        return steps
                
                for r, s in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    p, q = x + r, y + s
                    
                    if 0 <= p < m and 0 <= q < n and (p, q, found) not in visited:
                        visited.add((p, q, found))
                        
                        newStack.append((p, q, found, steps + 1))
                        
            stack = newStack
            
        return -1
        
