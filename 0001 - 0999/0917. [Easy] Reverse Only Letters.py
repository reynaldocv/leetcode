# https://leetcode.com/problems/reverse-only-letters/

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        seen = set()

        for i in range(26):
            seen.add(chr(ord("a") + i))
            seen.add(chr(ord("A") + i))
            
        tmp = ""
        
        for char in s: 
            if char in seen:
                tmp = char + tmp
                
        idx = 0 
        
        ans = ""
        
        for char in s: 
            if char in seen:
                ans += tmp[idx] 
                idx += 1 
                
            else: 
                ans += char
                
        return ans 
            
        
