# https://leetcode.com/problems/faulty-keyboard/

class Solution:
    def finalString(self, s: str) -> str:
        stack = []
        
        for char in s: 
            if char == "i":
                stack = stack[:: -1]
                
            else: 
                stack.append(char)
                
        return "".join(stack)
