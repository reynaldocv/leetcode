# https://leetcode.com/problems/remove-adjacent-almost-equal-characters/

class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int: 
        prev = "$"
        cnt = 0 
        
        ans = 0 
        
        for char in word + "$":
            tmp = abs(ord(char) - ord(prev))
            
            if tmp <= 1:
                cnt += 1 
                
            else: 
                ans += cnt//2
                
                cnt = 1
                
            prev = char
            
        return ans 
