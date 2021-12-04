# https://leetcode.com/problems/number-of-enclaves/

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def helper(i, j, val):
            grid[i][j] = val
            seen = {(i, j): True}
            stack = [(i, j)]
            while stack: 
                (i, j) = stack.pop()
                for (x, y) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= x < m and 0 <= y < n: 
                        if grid[x][y] == 1 and (x, y) not in seen: 
                            seen[(x, y)] = True
                            grid[x][y] = val
                            stack.append((x, y))
            
            return len(seen)
            
        ans = sum(sum(row) for row in grid)
        
        m, n = len(grid), len(grid[0])
        
        bounds= []
        for i in range(m):
            bounds.extend([(i, 0), (i, n - 1)])
        
        for j in range(1, n - 1):
            bounds.extend([(0, j), (m - 1, j)])
            
        for (i, j) in bounds:
            if grid[i][j] == 1: 
                ans -= helper(i, j, 2)
                
        return ans
                
