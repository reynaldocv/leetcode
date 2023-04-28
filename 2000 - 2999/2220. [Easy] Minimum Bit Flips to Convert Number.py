# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = 0 
        
        while start or goal: 
            if start % 2 != goal % 2: 
                ans += 1 
                
            start //= 2 
            goal //= 2 
            
        return ans 
        
