# https://leetcode.com/problems/longest-duplicate-substring/

class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        
        ans = ""
        
        j = 1
        
        for i in range(n):
            while s[i: i + j] in s[i + 1: ]:
                ans = s[i: i + j]
                
                j += 1
                
        return ans

class Solution2:
    def longestDupSubstring(self, s: str) -> str:
        def helper(k):
            power = pow(26, k, MOD)
            
            hash_ = 0 
            
            seen = defaultdict(lambda: set())
            
            for (ith, char) in enumerate(s):
                hash_ = (26*hash_ + value[char]) % MOD 
                
                if ith >= k: 
                    hash_ = (hash_ - value[s[ith - k]]*power) % MOD
                    
                if ith + 1 >= k: 
                    if hash_ in seen and s[ith + 1 - k: ith + 1] in seen[hash_]:
                        return s[ith + 1 - k: ith + 1]
                    
                    seen[hash_].add(s[ith + 1 - k: ith + 1])
                    
            return ""
        
        value = {chr(ord("a") + i): i + i for i in range(26)}
        
        MOD = 10**9 + 7
        
        start = 0 
        end = len(s)
        
        while end - start > 1: 
            mid = (end + start)//2
            
            if helper(mid): 
                start = mid 
                
            else: 
                end = mid 
                
        return helper(start)
