# https://leetcode.com/problems/remove-outermost-parentheses/

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        prev = ")"
        
        lvl = 1 
        
        ans = ""
        
        for char in s: 
            if prev == char: 
                if char == "(":
                    lvl += 1 
                    
                else: 
                    lvl -= 1 
                    
            if lvl != 1: 
                ans += char
                
            prev = char
                
        return ans 
        
            
