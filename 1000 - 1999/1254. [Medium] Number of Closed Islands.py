# https://leetcode.com/problems/number-of-closed-islands/

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def helper(x, y):
            stack = [(x, y)]

            grid[x][y] = 1

            while stack: 
                (x, y) = stack.pop() 

                for (r, s) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    p, q = x + r, y + s
                    if 0 <= p < m and 0 <= q < n: 
                        if grid[p][q] == 0: 
                            grid[p][q] = 1 
                            stack.append((p, q))
            
            return 1 

        m, n = len(grid), len(grid[0])
        
        stack = set()
        
        for i in range(m):
            stack.add((i, 0))
            stack.add((i, n - 1))

        for j in range(n):
            stack.add((0, j))
            stack.add((m - 1, j))

        for (x, y) in stack: 
            if grid[x][y] == 0: 
                helper(x, y)

        ans = 0 

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: 
                    ans += helper(i, j)

        return ans 
    
