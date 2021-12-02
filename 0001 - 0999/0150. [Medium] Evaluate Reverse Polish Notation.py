# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        n = len(tokens)
        for i in range(n):
            token = tokens[i]
            if token in "+-/*":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num1 - num2)
                elif token == "*":
                    stack.append(num1 * num2)
                else:
                    stack.append(num1 / num2)                
            else: 
                stack.append(token)
            
        return int(stack.pop())
                
            
            
        
