# https://leetcode.com/problems/find-subarrays-with-equal-sum/

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        prev = nums[0]
        
        seen = set()
        
        for (i, num) in enumerate(nums[1: ]):
            prev += num 
            
            if prev in seen: 
                return True 
            
            seen.add(prev)
            prev -= nums[i]
            
        return False 
        
