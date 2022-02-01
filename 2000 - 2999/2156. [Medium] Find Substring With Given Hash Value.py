# https://leetcode.com/problems/find-substring-with-given-hash-value/

class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        values = {chr(ord("a") + i): i + 1 for i in range(26)}
        
        n = len(s)
        aHash = 0
        temp = 1
        for i in range(k - 1):
            aHash += values[s[i]]*temp
            temp *= power
        
        l, r = 0, k - 1   
        
        while r < n:
            aHash += values[s[r]]*temp
            
            if aHash % modulo == hashValue:
                return s[l: r + 1]
            
            aHash -= values[s[l]]                
            aHash //= power
            l, r = l+ 1, r + 1
