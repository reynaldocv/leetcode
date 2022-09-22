# https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        def helper(arr1, arr2):
            seen = {}
        
            for (i, word1) in enumerate(arr1): 
                word2 = arr2[i]
                if word1 not in seen: 
                    seen[word1] = word2
                
                elif seen[word1] != word2:
                    return False 
            
            return True 
            
        arrS = s.split(" ")
        arrPattern = [char for char in pattern]
        
        m, n = len(pattern), len(arrS)
        
        if m != n: 
            return False
        
        return helper(arrS, arrPattern) and helper(arrPattern, arrS) 
        
                
        
