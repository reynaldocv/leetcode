# https://leetcode.com/problems/consecutive-characters/

class Solution:
    def maxPower(self, s: str) -> int:
        aux, ans, n, l = "", 0, len(s), 0
        for i in range(n):
            if aux == s[i]:
                l += 1
            else:
                l = 1
                aux = s[i]
            ans = max(ans, l)
        return ans
        
        
        
