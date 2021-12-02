# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n >= 3: 
            res = n % 3
            if res > 1:
                return False
            else: 
                n = n//3
                
        return True if n <= 1 else False
        
                
