# https://leetcode.com/problems/count-binary-substrings/

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        auxs = s[0]
        l = 1
        aux = []
        for i in range(1, len(s)):
            if auxs == s[i]:
                l += 1
            else: 
                aux.append(l)
                auxs = s[i]
                l = 1
        aux.append(l)
        ans = 0
        for i in range(0, len(aux) - 1):
            ans += min(aux[i], aux[i + 1])
            
        return ans
        
            
        
                    
