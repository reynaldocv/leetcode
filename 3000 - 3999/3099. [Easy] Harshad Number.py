# https://leetcode.com/problems/harshad-number/

class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:        
        aSum = 0
        
        tmp = x 
        
        while tmp: 
            aSum += (tmp % 10)
            
            tmp //= 10 
            
        return aSum if x % aSum == 0 else -1
        
