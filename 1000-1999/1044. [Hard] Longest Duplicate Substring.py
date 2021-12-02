# https://leetcode.com/problems/longest-duplicate-substring/

class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        result = ""
        j = 1
        
        for i in range(n):
            while s[i: i + j] in s[i + 1: ]:
                result = s[i: i + j]
                j += 1
                
        return result   
