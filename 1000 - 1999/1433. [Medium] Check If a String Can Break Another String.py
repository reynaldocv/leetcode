# https://leetcode.com/problems/check-if-a-string-can-break-another-string/

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        def helper(string1, string2):
            for i in range(n):
                if string1[i] > string2[i]:
                    return False 
                
            return True 
        
        n = len(s1)
        
        s1 = "".join(sorted(s1))
        s2 = "".join(sorted(s2))
        
        return helper(s1, s2) or helper(s2, s1)
                
        
