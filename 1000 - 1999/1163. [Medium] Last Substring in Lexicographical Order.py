# https://leetcode.com/problems/last-substring-in-lexicographical-order/

class Solution:
    def lastSubstring(self, s: str) -> str:        
        ans = chr(ord("a") - 1)
        prefix = ""
        for char in s[::-1]:
            prefix = char + prefix
            ans = max(ans, prefix)
            
        return ans
            
