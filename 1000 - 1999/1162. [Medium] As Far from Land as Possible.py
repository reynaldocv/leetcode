# https://leetcode.com/problems/as-far-from-land-as-possible/

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        stack = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]
        seen = {(i, j): True for i in range(n) for j in range(n) if grid[i][j] == 1}
        
        if len(stack) == n*n:
            return -1
        
        ans = 0
        while stack: 
            newStack = []
            for (x, y) in stack: 
                for (r, s) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= r < n and 0 <= s < n: 
                        if (r, s) not in seen: 
                            newStack.append((r, s))
                            seen[(r, s)] = True
            
            stack = newStack
            ans += 1
            
        return ans - 1
        
        
