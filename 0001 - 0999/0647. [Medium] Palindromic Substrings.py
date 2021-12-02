# https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0 
        for (i, val) in enumerate(s):
            ans += 1
            start = i
            end = i + 1
            while 0 <= start and end < n and s[start] == s[end]:
                ans += 1
                start -= 1
                end += 1
            center = i
            delta = 1 
            while 0 <= center - delta and center + delta < n and s[center - delta] == s[center + delta]:
                delta += 1
                ans += 1
        
        return ans
            
        
