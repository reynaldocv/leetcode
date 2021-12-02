# https://leetcode.com/problems/unique-substrings-in-wraparound-string/

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        n = len(p)
        
        dp = [1 for _ in range(n)]
        
        for i in  range(1, n):
            if (ord(p[i]) == (ord(p[i - 1]) + 1)) or (p[i] == 'a' and p[i - 1] == 'z'):
                dp[i] = dp[i - 1] + 1
        
        seen = {}
        for i in range(n):
            if p[i] in seen:
                seen[p[i]] = max(seen[p[i]], dp[i])
            else:
                seen[p[i]] = dp[i]
                
        return sum(seen.values())
            
        
