# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

class Solution:
    def minOperations(self, s: str) -> int:
        ans = 0
        bita, bitb = 0, 1
        n = len(s)
        for i in range(n):
            if int(s[i]) != bita: 
                ans += 1
            bita = 1 - bita          
                    
        return min(ans, n - ans)
            
            
        
