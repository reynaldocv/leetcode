# https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def helper(x, y):
            stack = [(x, y)]
            grid2[x][y] = 0 
            
            seen = {grid1[x][y]}
            
            while stack: 
                (x, y) = stack.pop() 
                
                for (r, s) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    p, q = x + r, y + s
                    
                    if 0 <= p < m and 0 <= q < n: 
                        if grid2[p][q] == 1: 
                            grid2[p][q] = 0 
                            
                            seen.add(grid1[p][q])
                            stack.append((p, q))
                            
            return len(seen) == 1 and 1 in seen
        
        m, n = len(grid1), len(grid1[0])
        
        ans = 0 
        
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    if helper(i, j):
                        ans += 1 
                        
        return ans
                    
        
