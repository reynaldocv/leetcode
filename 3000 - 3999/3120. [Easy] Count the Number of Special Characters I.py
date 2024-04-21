# https://leetcode.com/problems/count-the-number-of-special-characters-i/

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        seenUpper = set()
        seenLower = set()
        
        for char in word: 
            if char == char.upper(): 
                seenUpper.add(char)
                
            else: 
                seenLower.add(char)
                
        ans = 0 
                
        for char in seenLower:
            if char.upper() in seenUpper: 
                ans += 1 
                
        return ans 
                
                
