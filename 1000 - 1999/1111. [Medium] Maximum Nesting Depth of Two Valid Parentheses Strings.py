# https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ans = []
        left, right = 0, 0
        
        for char in seq:
            if char == '(': 
                ans.append(left)
                left = 1 - left
            else:
                ans.append(right)
                right = 1 - right
        
        return ans
            
        
        
