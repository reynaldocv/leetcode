# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def helper(word1, word2):
            seen = {}
            
            for (i, char1) in enumerate(word1):
                char2 = word2[i]
                
                if char1 not in seen: 
                    seen[char1] = char2
                elif seen[char1] != char2:
                    return False 
                    
            return True 
        
        return helper(s, t) and helper(t, s)
