# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def helper(capacity):
            prev = 0 
            ans = 0 
            for num in weights: 
                prev += num
                if prev > capacity: 
                    ans += 1
                    prev = num
                    
            return ans + 1 if prev > 0 else ans
        
        start = max(weights) - 1
        end = sum(weights)
        
        while end - start > 1: 
            m = (end + start)//2
            if helper(m) <= days:
                end = m
            else: 
                start = m
                
        return end
