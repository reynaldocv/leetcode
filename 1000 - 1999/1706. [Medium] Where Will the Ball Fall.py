# https://leetcode.com/problems/where-will-the-ball-fall/

♃class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        
        ans = [-1 for _ in range(n)] 
        
        for j in range(n): 
            k = j
            go = True
            
            for i in range(m):
                kk = k + grid[i][k]
                if not 0 <= kk < n or grid[i][k] * grid[i][kk] < 0: 
                    go = False
                    break
                k = kk 
                
            if go:
                ans[j] = k
                
        return ans 
