# https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:        
        while num >= 10:
            aux = 0
            while num > 0:
                aux += (num % 10)
                num = (num // 10)
            num = aux
        return num
            
        
