# https://leetcode.com/problems/determine-if-string-halves-are-alike/

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def helper(word):
            ans = 0 
            
            for char in word: 
                if char.lower() in "aeiou":
                    ans += 1 
                    
            return ans 
        
        n = len(s)
        
        return helper(s[: n//2]) == helper(s[n//2: ])
    
    
        
