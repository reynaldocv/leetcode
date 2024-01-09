# https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        dimensions.sort(key = lambda item: (item[0]**2 + item[1]**2, item[0]*item[1]))
        
        return dimensions[-1][0]*dimensions[-1][1]
        
