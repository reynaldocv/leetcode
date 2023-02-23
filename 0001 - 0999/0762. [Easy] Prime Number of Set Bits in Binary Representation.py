# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def helper(num):
            ans = 0 
            
            while num: 
                bit = num % 2
                
                if bit == 1: 
                    ans += 1 
                    
                num = num//2
                
            return ans 
               
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
        
        ans = 0
        
        for num in range(left, right + 1):
            if helper(num) in primes: 
                ans += 1 
                
        return ans 
