# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n: 
            unit = n % 3
            
            if unit > 1: 
                return False 
            
            n //= 3 
            
        return True 
                
