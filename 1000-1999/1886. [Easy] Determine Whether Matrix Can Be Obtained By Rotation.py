# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def isSame(matrixA, matrixB, n):                        
            for i in range(n):
                for j in range(n):
                    if matrixA != matrixB:
                        return False
            return True
        def rotate(matrixA, n):
            return [[matrixA[x][n - 1 - y] for x in range(n)] for y in range(n)]
        
        n = len(mat)
        aux, t = mat, target
        for i in range(4):
            aux = rotate(aux, n)
            if isSame(aux, t, n):
                return True
        return False
        
        return isSame(mat, t, n) or isSame(A, t, n) or isSame(B, t, n) or isSame(C, t, n)
        
