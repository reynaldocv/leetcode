# https://leetcode.com/problems/shortest-bridge/

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        (x, y) = next((i, j) for i in range(n) for j in range(n) if grid[i][j] == 1)
        
        stack = [(x, y)]
        seen = {(x, y): True}
        while stack: 
            (x, y) = stack.pop()
            for r, s in [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]: 
                if 0 <= r < n and 0 <= s < n:
                    if grid[r][s] == 1 and (r, s) not in seen: 
                        seen[(r, s)] = True
                        stack.append((r, s))
                        
        ans = 0
        
        stack = list(seen)
        
        while stack:
            newStack = []
            for (x, y) in stack: 
                for (r, s) in [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]: 
                    if 0 <= r < n and 0 <= s < n:
                        if (r, s) not in seen: 
                            if grid[r][s] == 1: 
                                return ans 
                               
                            newStack.append((r, s))
                            seen[(r, s)] = True
            stack = newStack
            ans += 1
                 
