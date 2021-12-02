# https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def numHours(speed):
            ans = 0 
            for pile in piles: 
                if pile % speed == 0: 
                    ans += pile//speed
                else: 
                    ans += pile//speed + 1
            return ans
        
        start = 0
        end = max(piles) + 2
        while end - start > 1: 
            m = (end + start)//2
            if numHours(m) <= h: 
                end = m
            else: 
                start = m 
                
        return end
                
        
