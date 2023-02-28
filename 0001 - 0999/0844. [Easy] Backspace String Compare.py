# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(word):
            stack = []
            
            for char in word:
                if char == "#":
                    if stack:
                        stack.pop()
                
                else:
                    stack.append(char)
            
            return "".join(stack)
        
        return helper(s) == helper(t)
                    
                
