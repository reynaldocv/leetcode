# https://leetcode.com/problems/fraction-addition-and-subtraction/ 

class Solution:
    def fractionAddition(self, expression: str) -> str:
        expression = expression.replace("+-", "-")  
        
        prev = (0, 1) 
        sign = 1 
        num, den = 0, 0
        isNum = True
        
        for char in expression + "+":
            if char.isdigit():
                if isNum: 
                    num = num*10 + int(char)
                else: 
                    den = den*10 + int(char)
            elif char in "+-":
                if prev != (0, 0):
                    prev = (prev[0] * den + sign * prev[1] * num, prev[1] * den)
                else: 
                    prev = (sign*num, den)
                    
                num, den = 0, 0
                sign = 1 if char == "+" else -1
                isNum = True                
            elif char == "/":
                isNum = False
                
        m = gcd(abs(prev[0]), prev[1])
        
        if m == 0: 
            return "0/1"
        
        return str(prev[0]//m) + "/"+ str(prev[1]//m)
