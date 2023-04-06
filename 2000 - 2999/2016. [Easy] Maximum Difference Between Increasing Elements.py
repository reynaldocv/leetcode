# https://leetcode.com/problems/maximum-difference-between-increasing-elements/

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        
        minimum = nums[0]
        
        ans = -1
        
        for i in range(1, n):
            if nums[i] > minimum:
                ans = max(ans, nums[i] - minimum)
                
            minimum = min(minimum, nums[i])
            
        return ans 
        
        
