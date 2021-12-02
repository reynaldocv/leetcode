# https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:        
        n = len(s)
        dic = {}
        ans, odd = 0, 0
        for i in s:
            dic[i] = dic.get(i, 0) + 1 
        for i in dic: 
            if dic[i] % 2 == 1: 
                ans += dic[i] - 1
                odd = 1
            else: 
                ans += dic[i]
        return ans + odd
        
     
                
