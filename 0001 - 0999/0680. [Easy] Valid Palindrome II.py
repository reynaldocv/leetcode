# https://leetcode.com/problems/valid-palindrome-ii/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s):
            if len(s)>= 1:
                return s == s[::-1]
            return False
        
        start, end = 0, len(s) - 1
        while s[start] == s[end] and start < end:
            start += 1
            end -= 1
        if end <= start:
            return True
        else: 
            return isPalindrome(s[start + 1: end + 1]) or isPalindrome(s[start: end])
        
