# https://leetcode.com/problems/lucky-numbers-in-a-matrix/

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        
        minimuns = [min(row) for row in matrix]
        
        tmp = [[matrix[i][j] for i in range(m)] for j in range(n)]
        
        maximuns = [max(row) for row in tmp]
        
        ans = []
        
        for i in range(m):
            for j in range(n):
                value = matrix[i][j]
                if value == minimuns[i] and value == maximuns[j]:
                    ans.append(value)
                    
        return ans         
        
