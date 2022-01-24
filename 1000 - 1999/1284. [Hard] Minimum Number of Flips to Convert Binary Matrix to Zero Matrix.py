# https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/

class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        def helper(matrix):
            return sum(sum(row) for row in matrix) == 0
            
        def collaborator(matrix, x, y):
            matrix[x][y] = 1 - matrix[x][y]
            for p, q in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= p < n and 0 <= q < m: 
                    matrix[p][q] = 1 - matrix[p][q]
               
        if helper(mat): 
            return 0
        
        n, m = len(mat), len(mat[0])
        points = [(i, j) for i in range(n) for j in range(m)]
        
        for i in range(n*m):
            for perm in permutations(range(n*m), i + 1):
                matrix = [[mat[i][j] for j in range(m)] for i in range(n)] 
                for j in perm: 
                    collaborator(matrix, points[j][0], points[j][1])
                    
                if helper(matrix):
                    return len(perm)
        
        return -1
                
                
            
            
