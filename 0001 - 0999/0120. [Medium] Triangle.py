# https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
    
        for lvl in range(n - 2, -1, -1):
            for j in range(lvl + 1):
                triangle[lvl][j] = min(triangle[lvl + 1][j], triangle[lvl + 1][j + 1]) + triangle[lvl][j]
                
        return triangle[0][0]
