# https://leetcode.com/problems/find-all-groups-of-farmland/

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def helper(x, y):
            start = (x, y)
            
            stack = [(x, y)]
            land[x][y] = 0 
            
            end = (x, y)
            
            while stack: 
                (x, y) = stack.pop() 
                
                end = max(end, (x, y))
                
                for (r, s) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    p, q = x + r, y + s
                    
                    if 0 <= p < m and 0 <= q < n: 
                        if land[p][q] == 1: 
                            land[p][q] = 0
                            
                            stack.append((p, q))
                            
            return end 
                        
        m, n = len(land), len(land[0])
        
        ans = []
        
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1: 
                    (r, s) = helper(i, j)
                    
                    ans.append([i, j, r, s])
                
        return ans 
                
                
                
            
        
   
        
            
