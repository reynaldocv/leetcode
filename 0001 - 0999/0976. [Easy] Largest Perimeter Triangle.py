# https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        
        nums.sort() 
        
        ans = 0 
        
        for i in range(1, n - 1):
            if nums[i] - nums[i - 1] < nums[i + 1] < nums[i] + nums[i - 1]:
                ans = max(ans, nums[i - 1] + nums[i] + nums[i + 1])
                
        return ans 
        
