# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: 
            return nums[0]
        elif n == 2: 
            return max(nums)
        else: 
            prev = 0 
            ans = 0
            for i in range(1, n):
                nums[i] = prev + nums[i]
                prev = max(nums[i - 1], prev)
                ans = max(nums[i], ans)
                
            return ans
