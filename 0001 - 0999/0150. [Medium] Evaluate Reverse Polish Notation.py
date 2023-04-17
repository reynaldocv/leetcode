# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens: 
            if token in "+-*/":
                num2 = str(stack.pop())
                num1 = str(stack.pop())
                
                stack.append(int(eval(num1 + token + num2)))
                
            else: 
                stack.append(int(token))
                
        return stack[-1]
        
            
            
        
