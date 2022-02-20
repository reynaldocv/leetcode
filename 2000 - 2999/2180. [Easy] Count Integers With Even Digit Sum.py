# https://leetcode.com/problems/count-integers-with-even-digit-sum/

class Solution:
    def countEven(self, num: int) -> int:
        def helper(number):
            ans = 0 
            while number > 0: 
                ans += (number % 10)
                number //= 10 
            
            return ans 
        
        number = 1
        ans = 0 
        
        while number <= num: 
            if helper(number) % 2 == 0:
                ans +=1 
            number += 1 
            
        return ans
        
