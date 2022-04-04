# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def helper(mat):
            for i in range(n):
                for j in range(i + 1, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
                    
            for i in range(n):
                for j in range(n//2):
                    mat[i][j], mat[i][n - 1 - j] = mat[i][n - 1 - j], mat[i][j]
            
        n = len(mat)
        for i in range(4):
            helper(mat)
            if mat == target: 
                return True 
            
        return False 
