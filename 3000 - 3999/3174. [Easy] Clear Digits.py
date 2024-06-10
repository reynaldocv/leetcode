# https://leetcode.com/problems/clear-digits/

class Solution:
    def clearDigits(self, s: str) -> str:
        arr = []
        
        for char in s: 
            if char.isdigit() and arr: 
                arr.pop()
                    
            else: 
                arr.append(char)
                
        return "".join(arr)
        
