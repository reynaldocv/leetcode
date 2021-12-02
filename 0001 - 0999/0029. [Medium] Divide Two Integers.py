# https://leetcode.com/problems/divide-two-integers/

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647 

        sign = -1 if dividend < 0 else 1         
        sign = sign*-1 if divisor < 0 else sign
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        ans = 0
        while dividend >= divisor: 
            quo = 1 
            aux = divisor
            while (aux << 1) <= dividend: 
                quo <<= 1
                aux <<= 1
            dividend -= aux
            ans += quo
        
        return sign*ans
        
        
