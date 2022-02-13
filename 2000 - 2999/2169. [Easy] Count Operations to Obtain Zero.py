# https://leetcode.com/problems/count-operations-to-obtain-zero/

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0 
        
        while num1 != 0 and num2 != 0:
            if num1 > num2: 
                num1 -= num2                
            else: 
                num2 -= num1
            ans += 1 
            
        return ans
