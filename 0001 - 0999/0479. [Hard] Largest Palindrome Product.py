# https://leetcode.com/problems/largest-palindrome-product/

class Solution:
    def largestPalindrome(self, n: int) -> int:                    
        MOD = 1337
        if n == 1: 
            return 9 
        
        ans = 0 
        for numA in range(10**n - 1, 10**(n - 1), -2):
            if numA*numA < ans: 
                break
                
            for numB in range(10**n - 1, numA, -2):
                product = numA*numB
                
                if product % 11 == 0: 
                    if str(product) == str(product)[::-1]:
                        ans = max(ans, product)
                        
        return ans % MOD
        
        
