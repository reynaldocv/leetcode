# https://leetcode.com/problems/number-of-changing-keys/

class Solution:
    def countKeyChanges(self, s: str) -> int:
        n = len(s)
        
        ans = 0
        
        for i in range(1, n):
            if s[i - 1].lower() != s[i].lower():
                ans += 1 
                
        return ans 
        
