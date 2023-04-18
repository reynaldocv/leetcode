# https://leetcode.com/problems/maximal-rectangle/

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def helper(arr):
            stack = [(-1, -1)]
            
            ans = 0 
            
            for (i, num) in enumerate(arr + [0]):
                while stack and stack[-1][0] > num: 
                    (elem, _) = stack.pop()
                    
                    (_, start) = stack[-1]
                    
                    ans = max(ans, elem*(i - start - 1))
                    
                stack.append((num, i))
                
            return ans 
        
        m, n = len(matrix), len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                matrix[i][j] = int(matrix[i][j])
                
                if matrix[i][j] != 0 and i > 0: 
                    matrix[i][j] = matrix[i][j] + matrix[i - 1][j]
                   
        ans = 0 
        
        for row in matrix:
            ans = max(ans, helper(row))
            
        return ans 
        
            
            
            
            
            
            
            
            
            
            
            
        
