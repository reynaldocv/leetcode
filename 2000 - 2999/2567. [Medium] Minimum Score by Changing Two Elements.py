# https://leetcode.com/problems/minimum-score-by-changing-two-elements/

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n <= 3: 
            return 0 
        
        nums.sort() 
        
        ans = min(nums[-1] - nums[0], nums[-2] - nums[1])
        
        ans = min(ans, nums[-1] - nums[1], nums[-1] - nums[2])
        ans = min(ans, nums[-2] - nums[0], nums[-3] - nums[0])        
        
        return ans 
