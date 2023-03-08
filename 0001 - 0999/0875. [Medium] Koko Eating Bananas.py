# https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(velocity):
            ans = 0 
            
            for pile in piles: 
                ans += pile//velocity
                
                if pile % velocity != 0: 
                    ans += 1 
                    
            return ans 
        
        start = 0
        end = sum(piles)
        
        while end - start > 1: 
            middle = (end + start)//2
            
            if helper(middle) <= h: 
                end = middle 
            
            else: 
                start = middle 
                
        return end
                
        
