# https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n, m = len(rowSum), len(colSum) 
        
        ans = [[0]*m for _ in range(n)] 
        
        i = j = 0
        while i < n and j < m:
            ans[i][j] = min(rowSum[i], colSum[j])
            
            rowSum[i] -= ans[i][j]
            colSum[j] -= ans[i][j]
            
            if rowSum[i] == 0: 
                i += 1
                
            if colSum[j] == 0: 
                j += 1
                
        return ans 
        
