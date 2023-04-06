# https://leetcode.com/problems/split-with-minimum-sum/

class Solution:
    def splitNum(self, num: int) -> int:
        digits = [char for char in str(num)]
        
        digits.sort() 
        
        turn = 1
        
        num1 = ""
        
        num2 = ""
        
        for digit in digits: 
            if turn: 
                num1 += digit
                
            else: 
                num2 += digit
                
            turn = 1 - turn 
            
        return int(num1) + int(num2)
