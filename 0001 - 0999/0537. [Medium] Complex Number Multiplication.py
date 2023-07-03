# https://leetcode.com/problems/complex-number-multiplication/

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def helper(word):
            num, cmp = 0, 0
            
            tmp = ""
            
            for char in word: 
                if char == "+":
                    num = int(tmp)
                    
                    tmp = ""
                    
                elif char == "i":
                    cmp = int(tmp)
                    
                else: 
                    tmp += char 
                    
            return num, cmp 
        
        number1, cmp1 = helper(num1)
        number2, cmp2 = helper(num2)
        
        return str(number1*number2 - cmp1*cmp2) + "+" +str(number1*cmp2 + number2*cmp1) + "i"
                    
            
            
