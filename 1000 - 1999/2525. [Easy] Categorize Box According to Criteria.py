# https://leetcode.com/problems/categorize-box-according-to-criteria/

class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        maxSide = max(length, width, height)
        
        volume = length*width*height
        
        bulky = True if maxSide >= 10000 or volume >= 1000000000 else False 
        heavy = True if mass >= 100 else False
        
        if bulky and heavy:
            return "Both"
        elif bulky:
            return "Bulky"
        elif heavy:
            return "Heavy"
        else: 
            return "Neither"
        
        
