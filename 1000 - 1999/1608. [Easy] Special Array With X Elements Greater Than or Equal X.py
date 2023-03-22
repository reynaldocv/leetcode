# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        @cache
        def helper(value):
            ans = 0 
            
            for num in nums: 
                if value <= num:
                    ans += 1 
                    
            return ans 
        
        start = -1 
        end = max(nums)
        
        while end - start > 1: 
            middle = (end + start)//2
            
            if middle <  helper(middle):
                start = middle 
                
            else:
                end = middle 
                
        return end if end == helper(end) else -1 
        
        
                    
                    
