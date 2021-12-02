# https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        start, ans = nums[0], 0
        
        for i in range(1, len(nums)):
            if start >= nums[i]:
                ans += start - nums[i] + 1
                start += 1
            else:
                start = nums[i]
        return ans
        
