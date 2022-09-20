# https://leetcode.com/problems/find-subarrays-with-equal-sum/

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen = {nums[0] + nums[1]}
        
        n = len(nums)
        
        for i in range(1, n - 1):
            tmp = nums[i] + nums[i + 1]
            
            if tmp in seen: 
                return True 
            
            seen.add(tmp)
            
        return False
