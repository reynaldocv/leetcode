# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m == 0: return True        
        idx = 0        
        for i in range(n):
            if s[idx] == t[i]:
                idx += 1
            if idx == m: 
                return True
        return False
                
