# https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def helper(word1, word2):
            seen = {}
            
            for (i, char) in enumerate(word1):
                if char in seen: 
                    if seen[char] != word2[i]:
                        return False 
                    
                seen[char] = word2[i]
                
            return True 
        
        ans = []
        
        for word in words: 
            if helper(word, pattern) and helper(pattern, word):
                ans.append(word)
                
        return ans 
                
            
                
        
                
        
