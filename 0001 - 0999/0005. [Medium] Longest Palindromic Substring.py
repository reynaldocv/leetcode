# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n, ans, nans = len(s), "", 0
        for i in range(n):
            j = 0
            while i - j >= 0 and i + j < n and s[i - j] == s[i + j]:
                j += 1
                if nans < 2*j - 1:
                    ans = s[i - j + 1: i + j]
                    nans = 2*j - 1
        
            j = 0
            while i - j >= 0 and i + j + 1 < n and s[i - j] == s[i + j + 1]:
                j += 1
                if nans < 2*j:
                    ans = s[i - j + 1: i + j + 1]
                    nans = 2*j
        return ans
        
                
