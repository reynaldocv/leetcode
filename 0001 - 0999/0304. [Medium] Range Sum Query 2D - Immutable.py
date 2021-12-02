# https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.n, self.m = len(matrix), len(matrix[0])        
        self.matSum = [[matrix[i][j] for j in range(self.m)] for i in range(self.n)]
        
        for i in range(1, self.n):
            self.matSum[i][0] += self.matSum[i - 1][0]
       
        for j in range(1, self.m):
            self.matSum[0][j] += self.matSum[0][j - 1]
            
        for i in range(1, self.n):
            for j in range(1, self.m):
                self.matSum[i][j] += self.matSum[i - 1][j] + self.matSum[i][j - 1] - self.matSum[i - 1][j - 1]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 -= 1
        col1 -= 1
        val1 = self.matSum[row2][col2]
        val2 = self.matSum[row1][col2] if row1 >= 0 else 0 
        val3 = self.matSum[row2][col1] if col1 >= 0 else 0 
        val4 = self.matSum[row1][col1] if col1 >= 0 and row1 >= 0 else 0 
        
        return val1 - val2 - val3 + val4
            
        
        
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
