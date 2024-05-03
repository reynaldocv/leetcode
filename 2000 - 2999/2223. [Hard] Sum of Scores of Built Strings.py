# https://leetcode.com/problems/sum-of-scores-of-built-strings/

class Solution:
    def sumScores(self, s: str) -> int:        
        MOD = 119_218_851_371
        
        n = len(s)
        
        prefix = [0]
        power = [1]
        
        value = {chr(ord("a") + i): i for i in range(26)}
        
        for char in s: 
            prefix.append((prefix[-1]*26 + value[char]) % MOD)
            power.append((power[-1]*26) % MOD) 
            
        ans = 0 
        
        for (ith, char) in enumerate(s):
            if s[0] == char: 
                start = ith 
                end = n 
                
                while end - start > 1: 
                    mid = (end + start)//2
                    
                    tmp = (prefix[mid + 1] - prefix[ith]*power[mid - ith + 1]) % MOD 
                    
                    if tmp == prefix[mid - ith + 1]:
                        start = mid 
                        
                    else: 
                        end = mid 
                        
                ans += end - ith 
                
        return ans 
    
