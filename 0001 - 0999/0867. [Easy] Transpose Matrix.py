# https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        ans = [[matrix[i][j] for i in range(n)] for j in range(m)]
        return ans
        
