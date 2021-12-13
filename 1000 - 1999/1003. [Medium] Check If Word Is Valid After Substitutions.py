# https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/

class Solution:
    def isValid(self, s: str) -> bool:
        prev = s + "abc"
        while prev != s: 
            prev = s 
            s = s.replace("abc", "")
            if prev == s: 
                break
                
        return s == ""
            
        
        
