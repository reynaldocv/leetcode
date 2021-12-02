# https://leetcode.com/problems/longest-valid-parentheses/

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s) 
        stack = []
        
        for (i, char) in enumerate(s): 
            if char == "(":
                stack.append(("(", i))
            elif char == ")":
                if stack and stack[-1][0] == "(":
                    stack.pop()
                else: 
                    stack.append((")", i))
            
        stack.append(("*", n))
        ans = n if not stack else stack[0][1] + 1
        for i in range(len(stack) - 1):
            ans = max(ans, stack[i + 1][1] - stack[i][1])
            
        return ans - 1
            
        
