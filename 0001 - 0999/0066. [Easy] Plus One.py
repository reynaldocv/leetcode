# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        tmp = 1
        
        for i in range(n - 1, -1, -1):
            aSum = digits[i] + tmp            
            digits[i] = (aSum % 10)            
            tmp = aSum // 10 
            
        if tmp: 
            digits.insert(0, 1)

        return digits
        
