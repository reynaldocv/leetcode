# https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/

class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        n = len(s)
        
        seen = set()
        
        for i in range(n - 1):
            seen.add(s[i: i + 2])
            
        tmp = s[:: -1]
        
        for i in range(n - 1):
            if tmp[i: i + 2] in seen: 
                return True 
            
        return False 
        
            
