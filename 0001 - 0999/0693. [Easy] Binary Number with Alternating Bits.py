# https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binString = str(bin(n))[2: ]
        
        n = len(binString)
        
        for i in range(1, n):
            if binString[i] == binString[i - 1]:
                return False 
            
        return True 
                   
            
