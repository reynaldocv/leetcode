# https://leetcode.com/problems/spiral-matrix-ii/

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for _ in range(n)] for _ in range(n)]
        
        val = 1 
        
        (x, y) = (0, -1)
        
        seen = {(0, n), (n, n - 1), (n - 1, -1)}
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        k = 0 
        
        while val <= n**2:
            x += directions[k][0]
            y += directions[k][1]
            
            if (x, y) in seen: 
                x -= directions[k][0]
                y -= directions[k][1]
                
                k = (k + 1) % 4 
            
            else: 
                ans[x][y] = val
                val += 1 
                
                seen.add((x, y))
                
        return ans 
                
                
        
        
