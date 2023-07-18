# https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        stack = [(i, 0) for i in range(m)]
        
        ans = 0
        
        while stack: 
            seen = set()
            newStack = []
            
            for (x, y) in stack: 
                for (r, s) in [(-1, 1), (0, 1), (+1, 1)]:
                    p, q = x + r, y + s
                    
                    if 0 <= p < m and 0 <= q < n: 
                        if grid[x][y] < grid[p][q] and (p, q) not in seen: 
                            seen.add((p, q))
                            
                            newStack.append((p, q))
                            
            stack = newStack 
            
            if len(stack) > 0: 
                ans += 1
            
        return ans 
