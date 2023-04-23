# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = 0
        
        first = None 
        second = None
        
        n = len(s1)
        
        for i in range(n):
            if s1[i] != s2[i]:
                if first: 
                    second = (s2[i], s1[i])
                
                else: 
                    first = (s1[i], s2[i])
                    
                diff += 1 
                
        if diff == 0: 
            return True 
        
        elif diff == 2: 
            return first == second
        
        return False
        
