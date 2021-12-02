# https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        
        for j in range(1, m):
            matrix[0][j] ^= matrix[0][j - 1]            
        
        for i in range(1, n):
            matrix[i][0] ^= matrix[i - 1][0]
            
        for i in range(1, n):
            for j in range(1, m):
                matrix[i][j] ^= matrix[i - 1][j]^matrix[i][j - 1]^matrix[i - 1][j - 1]
        
        ans = []
        for row in matrix: 
            ans.extend(row)
        
        ans.sort(reverse = True)
        return ans[k - 1]
