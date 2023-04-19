# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0 
        
        ans = 0 
        
        for char in s: 
            if char == "(":
                count += 1 
                
                ans = max(ans, count)
                
            elif char == ")":
                count -= 1 
                
        return ans 
        
