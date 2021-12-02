# https://leetcode.com/problems/scramble-string/

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def helper(s1, s2):
            if len(s1) == 1 and s1 == s2: 
                return True
            
            for i in range(1, len(s1)):
                if sorted(s1[:i]) == sorted(s2[:i]):
                    if helper(s1[:i], s2[:i]) and helper(s1[i:], s2[i:]):
                        return True
            
            s2 = s2[::-1]
            for i in range(1, len(s1)):
                if sorted(s1[:i]) == sorted(s2[:i]):
                    if helper(s1[:i], s2[:i]) and helper(s1[i:], s2[i:]):
                        return True
                    
            return False
        
        return helper(s1, s2)
                
                
        
        
        
