# https://leetcode.com/problems/make-three-strings-equal/

class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        n, m, l = len(s1), len(s2), len(s3)
        
        minElem = min(n, m , l)
        
        totalChars = 0
        
        for i in range(minElem):
            if s1[i] == s2[i] and s2[i] == s3[i]:
                totalChars += 3
                
            else: 
                break 
                
        if totalChars == 0: 
            return -1 
        
        else: 
            return m + n + l - totalChars
        
        
        
        
