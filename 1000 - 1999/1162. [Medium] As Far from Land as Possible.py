# https://leetcode.com/problems/as-far-from-land-as-possible/

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        stack = []
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: 
                    stack.append((i, j))
                    
        if not stack or len(stack) == m*n: 
            return -1
        
        ans = -1 
        
        while stack: 
            newStack = []
            for (x, y) in stack:
                for (r, s) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    p, q = x + r, y + s
                    
                    if 0 <= p < m and 0 <= q < n and grid[p][q] == 0: 
                        grid[p][q] = 1                        
                        newStack.append((p, q))
                        
            ans += 1 
            stack = newStack
            
        return ans 
        
        
        
