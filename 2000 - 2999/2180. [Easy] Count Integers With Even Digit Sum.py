# https://leetcode.com/problems/count-integers-with-even-digit-sum/

class Solution:
    def countEven(self, num: int) -> int:
        def helper(number):
            ans = 0 
            
            while number: 
                ans += (number % 10)
                
                number //= 10 
                
            return ans % 2 == 0 
        
        ans = 0 
        
        for number in range(2, num + 1):
            if helper(number):
                ans += 1 
                
        return ans 
            
            
                
        
