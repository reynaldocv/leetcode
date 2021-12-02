# https://leetcode.com/problems/maximal-rectangle/

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def helper(arr):
            arr.append(0)
            n = len(arr)
            stack = [0]
            ans = arr[0]
            for i in range(1, n):
                while stack and arr[stack[-1]] > arr[i]: 
                    hight = arr[stack.pop()]
                    start = stack[-1] if stack else -1
                    width = i - start - 1
                    ans = max(ans, width*hight)
                
                stack.append(i)
                
            return ans
            
        n = len(matrix)
        m = len(matrix[0]) if n >= 1 else 0 
        if n == 0: 
            return 0
        
        matrix = [[int(matrix[i][j]) for j in range(m)] for i in range(n)]
        for j in range(m):
            for i in range(1, n):
                if matrix[i][j] != 0: 
                    matrix[i][j] += matrix[i - 1][j]
        
        ans = 0
        for row in matrix: 
            ans = max(ans, helper(row))
            
        return ans
        
