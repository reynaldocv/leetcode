# https://leetcode.com/problems/largest-odd-number-in-string/

class Solution:
    def largestOddNumber(self, num: str) -> str:
        limit = 0
        
        for (i, char) in enumerate(num): 
            if int(char) % 2 == 1: 
                limit = i + 1 
                
        return num[: limit]
        
    
        
        
