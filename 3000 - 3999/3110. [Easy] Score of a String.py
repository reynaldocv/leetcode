# https://leetcode.com/problems/score-of-a-string/

class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0 
        
        prev = s[0]
        
        for char in s:
            ans += abs(ord(char) - ord(prev))
            
            prev = char
            
        return ans 
        
