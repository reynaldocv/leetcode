# https://leetcode.com/problems/maximum-difference-between-increasing-elements/

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        sMin = nums[0]
        ans = -inf
        n = len(nums)
        for i in range(1, n):
            ans = max(ans, nums[i] - sMin)
            sMin = min(sMin, nums[i])
        
        return ans if ans > 0 else -1
