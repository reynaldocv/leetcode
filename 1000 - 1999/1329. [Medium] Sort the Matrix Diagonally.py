# https://leetcode.com/problems/sort-the-matrix-diagonally/

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        starts = [(i, 0) for i in range(n)]
        starts.extend([(0, j) for j in range(1, m)])
        
        for (x, y) in starts: 
            aux = []
            r, s = x, y
            while 0 <= r < n and 0 <= s < m: 
                aux.append(mat[r][s])
                r, s = r + 1, s + 1
            aux.sort()
            for i in range(len(aux)):
                mat[x + i][y + i] = aux[i]
        
        return mat
                
