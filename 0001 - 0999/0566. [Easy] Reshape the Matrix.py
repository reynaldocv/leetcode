# https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        aux = []
        for i in range(len(mat)):
            aux.extend(mat[i])
        
        if r*c != len(aux):
            return mat
        q = len(aux)//c
        print(q)
        ans = []
        for i in range(q):            
            ans.append(aux[i*c: (i + 1)*c])
            
        return ans
        
        
