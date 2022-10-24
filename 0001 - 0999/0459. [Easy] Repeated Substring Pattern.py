# https://leetcode.com/problems/repeated-substring-pattern/

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        
        m = 0 
        tmp = ""
        
        for char in s[: n//2]: 
            tmp += char
            m += 1 
            
            if n % m == 0: 
                multiply = n//m
                
                if tmp*multiply == s: 
                    return True 
                
        return False
        
        
