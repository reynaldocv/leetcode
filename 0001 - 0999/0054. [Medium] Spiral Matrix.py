# https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        x, y = 0, 0 
        k = 0 
        
        seen = {(0, 0): True, (0, n): True, (m, n - 1): True, (m - 1, -1): True}
        ans = [matrix[0][0]]
        
        i = 1 
        
        while i < m*n:
            x += directions[k][0]
            y += directions[k][1]
            
            if (x, y) in seen: 
                x -= directions[k][0]
                y -= directions[k][1]
                k = (k + 1) % 4
                
            else: 
                ans.append(matrix[x][y])
                seen[(x, y)] = True
                i += 1 
                
        return ans
                
            
                
                
                
            
        
                    
                                       
        
