# https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n - 2):
            if nums[i + 1] - nums[i] < nums[i + 2] < nums[i] + nums[i + 1]:
                ans = max(ans, nums[i] + nums[i + 1] + nums[i + 2])
        
        return ans
        
