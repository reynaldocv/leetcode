# https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        m, n = len(words), len(s)
        
        if m != n: 
            return False 
        
        for i in range(m):
            if s[i] != words[i][0]:
                return False 
            
        return True 
        
