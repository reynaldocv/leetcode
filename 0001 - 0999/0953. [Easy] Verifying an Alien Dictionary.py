# https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        @cache
        def helper(word):
            ans = ""
            
            for char in word: 
                ans += seen[char]
                
            return ans
            
        seen = {}
        
        for (i, char) in enumerate(order):
            seen[char] = chr(ord("a") + i)
            
        n = len(words)
        
        for i in range(n - 1):
            if helper(words[i]) > helper(words[i + 1]):
                return False 
            
        return True
    
