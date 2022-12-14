# https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/

class Solution:
    def minTimeToType(self, word: str) -> int:
        index = {chr(ord("a") + i): i for i in range(26)}
        
        source = "a"
        
        ans = 0 
        
        for char in word: 
            difference = abs(index[char] - index[source])
            
            ans += 1 + min(difference, 26 - difference)
            
            source = char
            
        return ans 
        
        
            
        
