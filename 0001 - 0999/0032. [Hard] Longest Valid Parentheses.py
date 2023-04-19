# https://leetcode.com/problems/longest-valid-parentheses/

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        
        stack = []
        
        for (i, char) in enumerate(s): 
            if char == "(":
                stack.append(("(", i))
                
            elif stack and stack[-1][0] == "(": 
                stack.pop() 
                
            else: 
                stack.append((")", i))                
        
        stack.insert(0, ("_", -1))
        stack.append(("_", n))
        
        m = len(stack)
        
        ans = 0 
        
        for i in range(m - 1):
            ans = max(ans, stack[i + 1][1] - stack[i][1] - 1)
            
        return ans 
        
        
