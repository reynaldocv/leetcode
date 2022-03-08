# https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def helper(x, y):            
            stack = [(x, y)]
            grid2[x][y] = 0
            islands = {grid1[x][y]: True}
                
            while stack: 
                (x, y) = stack.pop()
                for (r, s) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= r < m and 0 <= s < n: 
                        if grid2[r][s] == 1: 
                            grid2[r][s] = 0
                            stack.append((r, s))
                            islands[grid1[r][s]] = True
                            
            return not 0 in islands
        
        m, n = len(grid1), len(grid1[0])
        
        ans = 0 
        
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1: 
                    if helper(i, j): 
                        ans += 1 
                        
        return ans 
                    
        
