# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        positions = {}
        for (i, val) in enumerate(s):
            if val in "()":
                if val == "(":
                    stack.append(("(", i))
                elif val == ")":
                    if stack and stack[-1][0] == "(":
                        stack.pop()
                    else: 
                        positions[i] = True
        
        for (val, i) in stack: 
            positions[i] = True
            
        ans = ""
        for (i, val) in enumerate(s):
            if i not in positions: 
                ans += val
        
        return ans
            
                                
        
