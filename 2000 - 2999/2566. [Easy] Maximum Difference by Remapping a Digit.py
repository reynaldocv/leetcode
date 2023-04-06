# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/

class Solution:
    def minMaxDifference(self, num: int) -> int:
        digit = None 
        
        greater = ""        
        
        for char in str(num):
            if digit:
                if char == digit:
                    greater += "9"
                    
                else: 
                    greater += char
            
            else:
                if char != "9":
                    digit = char 
                
                greater += "9"
                
        digit = str(num)[0] 
        
        lower = ""
        
        for char in str(num):
            if char == digit: 
                lower += "0"
                
            else: 
                lower += char

        return int(greater) - int(lower)
        
