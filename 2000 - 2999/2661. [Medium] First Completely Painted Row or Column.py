# https://leetcode.com/problems/first-completely-painted-row-or-column/

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0]) 
        
        positions = {}
        
        for i in range(m):
            for j in range(n):
                positions[mat[i][j]] = (i, j)
                
        row = defaultdict(lambda: 0)
        col = defaultdict(lambda: 0)
        
        for (i, num) in enumerate(arr):
            (r, c) = positions[num]
            
            row[r] += 1 
            col[c] += 1 
            
            if row[r] == n or col[c] == m: 
                return i 
            
        
