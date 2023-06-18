# https://leetcode.com/problems/sort-the-matrix-diagonally/

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        stack = []
        
        for i in range(m):
            stack.append((i, 0))
            
        for j in range(1, n):
            stack.append((0, j))
            
        for (x, y) in stack: 
            arr = []
            
            i, j = x, y
            
            while i < m and j < n: 
                arr.append(mat[i][j])
                
                i += 1 
                j += 1 
                
            arr.sort()
            
            i, j, idx = x, y, 0
            
            while i < m and j < n: 
                mat[i][j] = arr[idx]
                
                i += 1 
                j += 1 
                idx += 1 
                
        return mat
                
