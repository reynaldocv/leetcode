# https://leetcode.com/problems/count-the-digits-that-divide-a-number/

class Solution:
    def countDigits(self, num: int) -> int:
        ans = 0 
        
        for char in str(num):
            if num % int(char) == 0: 
                ans += 1 
                
        return ans 
        
