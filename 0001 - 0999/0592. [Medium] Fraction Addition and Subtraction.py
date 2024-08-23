# https://leetcode.com/problems/fraction-addition-and-subtraction/ 

class Solution:
    def fractionAddition(self, expression: str) -> str:
        (prevNum, prevDen) = (0, 1)
        (num, den) = (0, 1)
        
        prev = ""
        
        for char in expression + "+":
            if char in "+-":
                den = 1 if prev == "" else int(prev)
                
                prevNum = prevNum*den + num*prevDen
                prevDen = prevDen*den
                
                common = gcd(prevNum, prevDen)
                
                prevNum //= common
                prevDen //= common 
                
                prev = char
                
            elif char == "/":
                num = int(prev)
                
                prev = ""
                
            else: 
                prev += char 
                
        return str(prevNum) + "/" + str(prevDen)
    
