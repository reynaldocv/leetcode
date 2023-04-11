# https://leetcode.com/problems/thousand-separator/

class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n == 0: 
            return "0"
        
        ans = ""
        
        counter = 0 
        
        while n: 
            counter = (counter + 1) % 3
            
            digit = n % 10
            
            ans = str(digit) + ans
            
            if counter == 0: 
                ans = "." + ans
                
            n //= 10
                
        if ans[0] == ".":
            ans = ans[1: ]
            
        return ans
        
