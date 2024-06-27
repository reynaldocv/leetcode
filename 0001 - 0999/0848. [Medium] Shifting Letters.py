# https://leetcode.com/problems/shifting-letters/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        
        for i in range(n - 2, -1, -1):
            shifts[i] = (shifts[i] + shifts[i + 1]) % 26
            
        index = {chr(ord("a") + i): i for i in range(26)}
        chars = {i: chr(ord("a") + i) for i in range(26)}
        
        ans = ""
        
        for i in range(n):
            ans += chars[(index[s[i]] + shifts[i]) % 26]
            
        return ans 
        
        
        
