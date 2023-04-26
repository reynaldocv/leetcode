# https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        def helper(number):
            ans = 0 
            
            while number: 
                ans += (number % 10)
                
                number //= 10 
                
            return ans 
        
        while num >= 10:
            num = helper(num)
            
        return num
            
            
        
