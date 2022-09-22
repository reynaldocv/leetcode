# https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        @cache
        def helper(x):
            ans = 0 
            
            while x: 
                ans += (x % 10)
                x //= 10 
                
            return ans 
        
        while num >= 10:
            num = helper(num)
            
        return num 
            
            
        
