# https://leetcode.com/problems/special-positions-in-a-binary-matrix/

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        mat2 = [[mat[i][j] for i in range(n)] for j in range(m)]
        
        print(mat, mat2)
        
        aux = [sum(mat[i]) for i in range(n)]
        aux2 = [sum(mat2[i]) for i in range(m)]
        
        ans = 0
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    if aux[i] == 1 and aux2[j] == 1:
                        ans += 1
        return ans
