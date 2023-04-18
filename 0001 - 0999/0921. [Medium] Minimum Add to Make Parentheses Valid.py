# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        
        for char in s: 
            if char == "(":
                stack.append("(")
                
            elif stack and stack[-1] == "(": 
                stack.pop() 
                
            else: 
                stack.append(")")
                
        return len(stack)
                
