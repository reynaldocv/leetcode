# https://leetcode.com/problems/percentage-of-letter-in-string/

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        total = 0 
        cnt = 0 
        for char in s: 
            if char == letter: 
                cnt += 1 
            
            total += 1 
            
        ans = 100*cnt//total
        
        return ans 
