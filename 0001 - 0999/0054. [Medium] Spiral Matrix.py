# https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        k = 0 
        
        (x, y) = (0, -1)
        
        seen = {(0, n), (m, n - 1), (m - 1, -1)}
        
        ans = []
        
        while len(ans) < m*n: 
            x += directions[k][0]
            y += directions[k][1]
            
            if (x, y) in seen: 
                x -= directions[k][0]
                y -= directions[k][1]
                
                k = (k + 1) % 4
                
            else: 
                ans.append(matrix[x][y])
                
                seen.add((x, y))
                
        return ans 
                
            
                
            
                
                
                
            
        
                    
                                       
        
