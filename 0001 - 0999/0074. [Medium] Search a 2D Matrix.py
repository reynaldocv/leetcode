# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def searchBinary(arr, target):
            start = 0 
            end = len(arr)
            while end - start > 1:             
                m = (end + start)//2
                if target < arr[m]:
                    end = m 
                else: 
                    start = m 
            return start, end
            
        n = len(matrix)
        m = len(matrix[0])
        
        row = -1
        for i in range(n):
            if matrix[i][0] <= target <= matrix[i][m - 1]:
                row = i
                break
        
        if row == -1: 
            return False
        else: 
            start, end = searchBinary(matrix[row], target)     
            return True if matrix[row][start] == target else False
    
