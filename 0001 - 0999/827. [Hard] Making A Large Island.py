# https://leetcode.com/problems/making-a-large-island/

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def helper(x, y, idx):
            seen = {(x, y): True}
            stack = [(x, y)]
            grid[x][y] = idx
            while stack: 
                (x, y) = stack.pop(0)
                for (r, s) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= r < m and 0 <= s < m: 
                        if (r, s) not in seen and grid[r][s] == 1:
                            seen[(r, s)] = True
                            stack.append((r, s))
                            grid[r][s] = idx
            
            areas[idx] = len(seen)
            
        m = len(grid)
        idx = 1
        areas = defaultdict(lambda: 0)
        for i in range(m):
            for j in range(m):
                if grid[i][j] == 1: 
                    idx += 1        
                    helper(i, j, idx)
        
        ans = areas[2] if 2 in areas else 0 
        for i in range(m):
            for j in range(m):
                if grid[i][j] == 0:
                    seen = {}
                    area = 0
                    for (r, s) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                        if 0 <= r < m and 0 <= s < m and grid[r][s] not in seen: 
                            seen[grid[r][s]] = True
                            area += areas[grid[r][s]]
                    
                    ans = max(ans, area + 1)
                    
        return ans
                    
