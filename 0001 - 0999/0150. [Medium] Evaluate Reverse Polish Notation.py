# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens: 
            if token in "+-*/":
                num2 = str(int(stack.pop()))
                num1 = str(int(stack.pop()))
                
                stack.append(eval(num1 + token + num2))
                
            else: 
                stack.append(token)
                
        return stack[-1]
        
                
            
            
        
