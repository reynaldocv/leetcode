# https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/

class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        
        ans = 0 
        
        for i in range(n//2):
            if s[2*i] != s[2*i + 1]:
                ans += 1 
                
        return ans 
        
