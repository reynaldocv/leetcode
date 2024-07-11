# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        word = ""
        
        for char in s: 
            if char == "(":
                stack.append(word)
                stack.append("(")
                               
            elif char == ")": 
                tmp = ""
                
                while stack and stack[-1] != "(":
                    tmp = stack.pop() + tmp
                    
                stack.pop() 
                
                stack.append(tmp[:: -1])
                
            else: 
                if stack and stack[-1] != "(":
                    stack[-1] += char
                
                else: 
                    stack.append(char)
                
        return "".join(stack)
                
               
            
