# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        start = 0
        end = m 
        
        while end - start > 1: 
            middle = (end + start)//2
            
            if matrix[middle][0] <= target: 
                start = middle 
                
            else: 
                end = middle 
                
        row = start
        
        start = -1
        end = n 
        
        while end - start > 1:
            middle = (end + start)//2
            
            if matrix[row][middle] < target: 
                start = middle 
                
            else: 
                end = middle 
                
        if end < n:
            return matrix[row][end] == target
        
        return False 
    
class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        stack = [(0, 0)]
        seen = {(0, 0)}
        
        while stack: 
            (x, y) = stack.pop()
            
            if matrix[x][y] == target: 
                return True
            
            for (r, s) in [(1, 0), (0, 1)]:
                p, q = x + r, y + s 
                
                if 0 <= p < m and 0 <= q < n: 
                    if matrix[p][q] <= target: 
                        if (p, q) not in seen: 
                            seen.add((p, q))
                            stack.append((p, q))
                            
        return False
    
