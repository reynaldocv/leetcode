# https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/

class Solution:
    def greatestLetter(self, s: str) -> str:
        seen = set()
        
        for char in s: 
            seen.add(char)
            
        ans = ""    
        
        for i in range(26):
            lower = chr(ord("a") + i)
            upper = chr(ord("A") + i)
            
            if lower in seen and upper in seen: 
                ans = max(ans, upper)
                
        return ans
