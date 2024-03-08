# https://leetcode.com/problems/maximum-matrix-sum/

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        aSum = 0 
        minElem = inf 
        
        counter = 0 
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] < 0: 
                    counter = (counter + 1) % 2
                    
                aSum += abs(matrix[i][j])
                
                minElem = min(minElem, abs(matrix[i][j]))
                
        if counter == 0: 
            return aSum 
        
        else: 
            return aSum - 2*minElem 
        
        
        
        
