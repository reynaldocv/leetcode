# https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def helper(x, y):
            stack = [(x, y)]
            grid[x][y] = 0 

            ans = 1 

            while stack: 
                (x, y) = stack.pop() 

                for (r, s) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    p, q = x + r, y + s

                    if 0 <= p < m and 0 <= q < n:
                        if grid[p][q] == 1: 
                            grid[p][q] = 0 
                            stack.append((p, q))
                            
                            ans += 1 

            return ans 
        
        m, n = len(grid), len(grid[0])

        ans = 0 

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: 
                    ans = max(ans, helper(i, j))

        return ans
