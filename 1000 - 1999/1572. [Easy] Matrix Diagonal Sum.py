# https://leetcode.com/problems/matrix-diagonal-sum/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l = len(mat)
        ans = 0
        for i in range(l):
            ans += mat[i][i]
            ans += mat[l - i - 1][i]
        if l % 2 == 1:
            ans -= mat[l//2][l//2]
        return ans
            
            
        
