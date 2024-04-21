# https://leetcode.com/problems/count-the-number-of-special-characters-ii/

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last = {}
        first = {}
        
        for (i, char) in enumerate(word): 
            if char == char.lower(): 
                last[char] = i 
                
            else: 
                if char not in first: 
                    first[char] = i 
                    
        ans = 0                 
    
        for char in last: 
            if char.upper() in first and last[char] < first[char.upper()]:
                ans += 1 
                
        return ans 
        
