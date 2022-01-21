# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0 
        while a or b or c: 
            if ((a & 1) or (b & 1)) != (c & 1):             
                if (c & 1) == 1: 
                    ans += 1
                elif (c & 1) == 0: 
                    ans += (a & 1) + (b & 1)
            
            a >>= 1
            b >>= 1
            c >>= 1
            
        return ans
                    
            
            
        
