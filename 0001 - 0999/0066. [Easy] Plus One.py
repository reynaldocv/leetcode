# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        aux, n = 1, len(digits)
        for i in range(n -1, -1, -1):
            dig = digits[i] + aux
            if dig >= 10:
                digits[i] = 0
                aux = 1
            else: 
                digits[i] = dig
                aux = 0
        if aux == 1: 
            digits.insert(0, 1)
        return digits
        
