# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0 
        
        while a or b or c: 
            unitA = a % 2
            unitB = b % 2 
            unitC = c % 2 
                        
            if (unitA or unitB) != unitC: 
                if unitC == 1: 
                    ans += 1
                    
                else: 
                    ans += (unitA + unitB)
                    
            a //= 2 
            b //= 2 
            c //= 2 
            
        return ans 
            
            
        
