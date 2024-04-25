# https://leetcode.com/problems/longest-happy-prefix/

class Solution:
    def longestPrefix(self, s: str) -> str:
        MOD = 10**9 + 7 
        
        n = len(s) 
        
        value = {chr(ord("a") + i): i for i in range(26)}
        
        prefix = 0 
        suffix = 0 
        
        power = 1
        
        end = -1
        
        for i in range(n - 1):
            prefix = (26*prefix + value[s[i]]) % MOD 
            suffix = (power*value[s[n - 1 - i]] + suffix) % MOD 
            
            if prefix == suffix: 
                if s[: i + 1] == s[n - 1 - i: ]:
                    end = i 
            
            power = (power*26) % MOD 
            
        return s[: end + 1]
