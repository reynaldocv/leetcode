# https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s: 
            if char == "c":
                if len(stack) > 1 and stack[-1] == "b" and stack[-2] == "a":
                    stack.pop() 
                    stack.pop() 
                
                else: 
                    return False 
                    
            else: 
                stack.append(char)
                
        return len(stack) == 0
