# https://leetcode.com/problems/check-if-the-number-is-fascinating/

class Solution:
    def isFascinating(self, n: int) -> bool:
        tmp = str(n) + str(2*n) + str(3*n)
        
        seen = {"0"}
        
        for char in tmp: 
            if char in seen: 
                return False 
            
            seen.add(char)

        return True  
