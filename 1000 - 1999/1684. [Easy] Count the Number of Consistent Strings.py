# https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        seen = set()
        
        for char in allowed: 
            seen.add(char)
            
        ans = 0 
        
        for word in words:
            go = True 
            
            for char in word: 
                if char not in seen: 
                    go = False 
                    break
                    
            if go: 
                ans += 1 
                
        return ans 
        
        
