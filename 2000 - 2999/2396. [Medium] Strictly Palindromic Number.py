# https://leetcode.com/problems/strictly-palindromic-number/

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return False 
        
class Solution2:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def helper(num, base):
            ans = ""
            
            while num > 0: 
                ans += str(num % base)
                num //= base 
                
            return ans == ans[::-1]
        
        for base in range(2, n - 1):
            if not helper(n, base):
                return False 
            
        return True 
