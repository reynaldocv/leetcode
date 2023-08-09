# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def helper(value):
            cnt = 0 
            
            i = 0 
            
            while i < n - 1: 
                if nums[i + 1] - nums[i] <= value: 
                    cnt += 1 
                 
                    i += 1 
                    
                i += 1 
                
            return cnt >= p
        
        n = len(nums)
        
        nums.sort()
        
        start = -1
        end = nums[-1] - nums[0]
        
        while end - start > 1: 
            middle = (end + start)//2
            
            if helper(middle):
                end = middle 
                
            else: 
                start = middle 
                
        return end 
