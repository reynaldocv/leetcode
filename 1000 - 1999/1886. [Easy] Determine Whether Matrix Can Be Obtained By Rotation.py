# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def helper(matrix):
            for i in range(n):
                for j in range(i, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                    
            for i in range(n//2):
                matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]
                
            return matrix
            
        n = len(mat)
        
        for _ in range(4):
            mat = helper(mat)
            
            if mat == target: 
                return True 
            
        return False 
