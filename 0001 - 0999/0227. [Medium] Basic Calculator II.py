# https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        
        num = 0 
        operation = "+"
        
        for char in s + "+":
            if char in "0123456789":
                num = 10*num + int(char)
                
            elif char in "+-*/":
                if operation == "+":
                    stack.append(num)
                
                elif operation == "-":
                    stack.append(-num)
                    
                elif operation == "*":
                    stack.append(stack.pop()*num)
                    
                else: 
                    stack.append(int(stack.pop()/num))
                
                num = 0             
                operation = char           
                
        return sum(stack)
                    
            
            
            
