# https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ans = (0, 0)
        
        for (length, width) in dimensions: 
            ans = max(ans, (length**2 + width**2, length*width))
            
        return ans[1]
