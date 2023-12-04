# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        
        k = k % n
        
        for i in range(m): 
            if mat[i] != mat[i][k: ] + mat[i][: k]:
                return False 
            
        return True 
        
