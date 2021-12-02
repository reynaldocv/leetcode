# https://leetcode.com/problems/maximum-matrix-sum/

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        totalNeg = 0
        totalSum = 0
        minElem = abs(matrix[0][0])
        for i in range(n):
            for j in range(n):
                minElem = min(minElem, abs(matrix[i][j]))
                if matrix[i][j] < 0:
                    totalNeg += 1
                totalSum += abs(matrix[i][j])
        
        if totalNeg % 2 == 1:
            totalSum -= 2*minElem
        
        return totalSum
            
        
