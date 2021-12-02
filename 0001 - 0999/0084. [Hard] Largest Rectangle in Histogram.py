# https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        n = len(heights)
        
        stack = [0]
        ans = heights[0]
        
        for i in range(1, n):
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                start = stack[-1] if stack else -1
                width = i - start - 1
                ans = max(ans, height*width)
                
            stack.append(i)
            
        return ans
