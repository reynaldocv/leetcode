# https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/

class Solution:
    def minChanges(self, n: int, k: int) -> int:
        ans = 0 
        
        while k > 0 or n > 0: 
            bit1 = k & 1 
            bit2 = n & 1
            
            if bit2 == 1:
                if bit1 == 0: 
                    ans += 1 
                    
            elif bit1 == 1: 
                return -1 
            
            n //= 2 
            k //= 2 
            
        return ans 
                
