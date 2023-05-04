# https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        
        for i in range(1, n):
            for j in range(i + 1):
                left = triangle[i - 1][j - 1] if j - 1 >= 0 else inf 
                right = triangle[i - 1][j] if j < i else inf 
                
                triangle[i][j] += min(left, right)
                
        return min(triangle[-1])

        
