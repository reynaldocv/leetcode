# https://leetcode.com/problems/spiral-matrix-iii/

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        x, y = rStart, cStart
        
        ans = [(x, y)]        
        seen = {(x, y): True}
        k = 0 
        
        while len(ans) < rows*cols: 
            x, y = x + directions[k][0], y + directions[k][1]
            if (x, y) not in seen: 
                if 0 <= x < rows and 0 <= y < cols: 
                    ans.append((x, y))
                    
                seen[(x, y)] = True
                k = (k + 1) % 4 
            else: 
                x, y = x - directions[k][0], y - directions[k][1]
                k = (k - 1) % 4
            
        return ans
