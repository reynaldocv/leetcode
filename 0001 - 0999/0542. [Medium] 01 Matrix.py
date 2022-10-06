# https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        stack = [(i, j) for i in range(m) for j in range(n) if mat[i][j] == 0]
        
        seen = {(i, j) for i in range(m) for j in range(n) if mat[i][j] == 0}
        
        distance = 1 
        
        while stack: 
            newStack = []
            
            for (x, y) in stack: 
                for (r, s) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    p, q = x + r, y + s
                
                    if 0 <= p < m and 0 <= q < n: 
                        if (p, q) not in seen: 
                            mat[p][q] = distance
                            newStack.append((p, q))
                            seen.add((p, q))
                            
            stack = newStack
            distance += 1 
            
        return mat
