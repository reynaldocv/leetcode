# https://leetcode.com/problems/minimize-string-length/

class Solution:
    def minimizedStringLength(self, s: str) -> int:
        seen = set()
        
        for char in s: 
            seen.add(char)
            
        return len(seen)
