# https://leetcode.com/problems/number-of-different-integers-in-a-string/

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        seen = set()
        
        num = ""
        
        for char in word + "a":
            if char in "0123456789":
                num += char 
                
            elif num: 
                seen.add(int(num))
                
                num = ""
                
        return len(seen)
        
        
        
        
