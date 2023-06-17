# https://leetcode.com/problems/search-a-2d-matrix-ii/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        if matrix[0][0] > target: 
            return False 

        stack = [(0, 0)]
        seen = {(0, 0)}

        while stack: 
            (x, y) = stack.pop()
            
            if matrix[x][y] == target: 
                return True 
            
            for (r, s) in [(1, 0), (0, 1)]:
                p, q = x + r, y + s
                
                if 0 <= p < m and 0 <= q < n:                 
                    if (p, q) not in seen and matrix[p][q] <= target: 
                        seen.add((p, q))

                        stack.append((p, q))

        return False 
            
            
