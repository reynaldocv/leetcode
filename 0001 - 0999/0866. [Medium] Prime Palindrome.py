# https://leetcode.com/problems/prime-palindrome/

class Solution:
    def primePalindrome(self, n: int) -> int:
        def isPrime(n):
            ans = True 
            limit = int(n**.5) 
            for i in range(3, limit + 1, 2):
                if n % i == 0: 
                    return False
                
            return ans
        
        if n <= 2: 
            return 2
        
        n += 1 if n % 2 == 0 else 0 
        
        while True: 
            if str(n) == str(n)[::-1]:
                if isPrime(n):
                    return n
            
            if 10**7 < n < 10**8: 
                n = 10**8 - 1
                
            n += 2
            
            
