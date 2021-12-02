# https://leetcode.com/problems/toeplitz-matrix/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        begin = [(0, i) for i in range(m)]
        begin.extend([(i, 0) for i in range(1, n)])
        min_ = min(n, m)
        ans = True 
        print(begin)
        for (x, y) in begin:
            aux = matrix[x][y]
            for j in range(1, min_):
                if x + j < n and y + j < m:
                    if aux != matrix[x + j][y + j]:
                        ans = False
                        break
            if not ans:
                break 
        return ans
                    
                
