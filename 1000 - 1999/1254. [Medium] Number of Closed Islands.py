# https://leetcode.com/problems/number-of-closed-islands/

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def helper(x, y, val):
            stack = [(x, y)]
            seen = {(x, y): True}
            grid[x][y] = val
            while stack: 
                (x, y) = stack.pop()
                for (r, s) in[(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= r < n and 0 <= s < m and grid[r][s] == 0:
                        if (r, s) not in seen: 
                            seen[(r, s)] = True
                            grid[r][s] = val
                            stack.append((r, s))
            
        n, m = len(grid), len(grid[0])
        
        arr = [(i, 0) for i in range(n)]
        arr.extend([(i, m - 1) for i in range(1, n - 1)])
        arr.extend([(0, j) for j in range(m)])
        arr.extend([(n - 1, j) for j in range(1, m - 1)])

        for (x, y) in arr: 
            if grid[x][y] == 0: 
                helper(x, y, 1)
                
        ans = 1
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if grid[i][j] == 0: 
                    ans += 1
                    helper(i, j, ans)
                    
        return ans - 1
        
        
        
