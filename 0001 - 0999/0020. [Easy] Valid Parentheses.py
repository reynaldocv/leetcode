# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s: 
            if char in "([{":
                stack.append(char)
            elif char == ")":
                if stack and stack[-1] == "(":
                    stack.pop() 
                else: 
                    return False 
            elif char == "]":
                if stack and stack[-1] == "[":
                    stack.pop() 
                else: 
                    return False 
            elif char == "}":
                if stack and stack[-1] == "{":
                    stack.pop() 
                else: 
                    return False 
                        
        return len(stack) == 0
