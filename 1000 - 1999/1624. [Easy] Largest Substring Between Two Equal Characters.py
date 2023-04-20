# https://leetcode.com/problems/largest-substring-between-two-equal-characters/

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = {}
        
        ans = -1
        
        for (i, char) in enumerate(s): 
            if char in seen:
                ans = max(ans, i - seen[char] - 1)
                
            if char not in seen: 
                seen[char] = i 
                
        return ans 
                
        
        
