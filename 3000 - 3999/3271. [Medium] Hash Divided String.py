# https://leetcode.com/problems/hash-divided-string/

class Solution:
    def stringHash(self, s: str, k: int) -> str:
        n = len(s)
        
        value = {chr(ord("a") + i): i for i in range(26)}
        letter = {i: chr(ord("a") + i) for i in range(26)}
        
        ans = ""
        
        for i in range(n//k):
            aSum = 0 
            
            for j in range(k*i, k*(i + 1)):
                aSum += value[s[j]]
        
            aSum %= 26 
            
            ans += letter[aSum]
        
        return ans 
        
