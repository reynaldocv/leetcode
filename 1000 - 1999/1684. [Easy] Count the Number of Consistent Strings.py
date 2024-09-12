# https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        seen = set()
        
        for char in allowed: 
            seen.add(char)
            
        ans = 0 
        
        for word in words:
            if all([char in seen for char in word]):
                ans += 1 
                
        return ans 
        
        
        
