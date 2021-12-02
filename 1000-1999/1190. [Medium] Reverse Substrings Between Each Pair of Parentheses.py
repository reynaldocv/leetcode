# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        word = ""
        for char in s + "$": 
            if char.isalpha():
                word += char
            elif char == "(":
                stack.append(word)
                stack.append("(")
                word = ""
            elif char == ")":
                aux = word
                while stack and stack[-1] != "(":
                    aux = stack.pop() + aux
                
                stack.pop()
                stack.append(aux[::-1])
                word = ""
            else: 
                stack.append(word)
            
        return "".join(stack)
                    
            
