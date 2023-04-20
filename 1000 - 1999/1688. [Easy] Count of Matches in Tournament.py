# https://leetcode.com/problems/count-of-matches-in-tournament/

class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0 
        
        while n > 1:
            ans += n//2    
            
            if n % 2 == 0:                 
                n = n//2
                
            else: 
                n = (n + 1)//2
        
        return ans 
