# https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(-1, -1)]
        
        ans = 0 
        
        for (i, height) in enumerate(heights + [0]):
            while stack[-1][0] >= height:                 
                (elem, _) = stack.pop()
                
                start = stack[-1][1]
                
                ans = max(ans, elem*(i - start - 1))
        
            stack.append((height, i))
            
        return ans 
    
