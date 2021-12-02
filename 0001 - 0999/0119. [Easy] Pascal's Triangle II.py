https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n = rowIndex + 1
        pascal = [[1]*i for i in range(1, n + 1)]
        
        for i in range(2, n):
            for j in range(1, len(pascal[i]) - 1):
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
        
        return pascal[n - 1]   
