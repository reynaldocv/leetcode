# https://leetcode.com/problems/minimum-additions-to-make-valid-string/

class Solution:
    def addMinimum(self, word: str) -> int:
        n = len(word)
        
        i = 0 
        
        j = 0 
        
        pattern = "abc"
        
        ans = 0 
        
        while i < n: 
            if word[i] == pattern[j]:
                i += 1
                
            else: 
                ans += 1 
                
            j = (j + 1) % 3
        
        ans += (3 - j) % 3
        
        return ans 
