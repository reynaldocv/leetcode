# https://leetcode.com/problems/repeated-substring-pattern/

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        
        prev = ""
        
        for char in s[: n//2]:
            prev += char 
            
            if n % len(prev) == 0: 
                if prev*(n//len(prev)) == s: 
                    return True 
                
        return False 
        
        
