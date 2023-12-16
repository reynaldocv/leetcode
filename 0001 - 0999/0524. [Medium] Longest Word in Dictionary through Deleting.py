# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        ans = (0, "")
        
        n = len(s)
        
        for word in dictionary:
            i, j = 0, 0
            
            m = len(word)
            
            while i < n and j < m:
                if word[j] == s[i]:
                    j += 1
                    
                i += 1
                
            if j == m:
                if ans[0] == m: 
                    ans = (m, min(ans[1], word))
                    
                else: 
                    ans = max(ans, (m, word))
                
        return ans[1]
            
        
        
