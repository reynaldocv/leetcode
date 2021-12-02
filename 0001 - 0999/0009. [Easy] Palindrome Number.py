# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        x = str(x)
        y = x[::-1]
        return x == y
        
        
