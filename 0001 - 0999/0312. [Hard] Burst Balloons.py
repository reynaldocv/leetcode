# https://leetcode.com/problems/burst-balloons/

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        @cache
        def helper(left, right):
            if left > right:
                return 0
            
            maximum = -inf
            
            for j in range(left, right + 1):
                maxLeft = helper(left, j - 1)  
                maxRight = helper(j + 1, right)
                auxMax = nums[j]*nums[left - 1]*nums[right + 1] + maxLeft + maxRight
                maximum = max(maximum, auxMax)
            
            return maximum
        
        n = len(nums)
        
        if min(nums) == max(nums):
            num = nums[0]
            if n == 1:
                return num
            
            return (n - 2)*num**3 + num**2 + num

        nums = [1] + nums + [1]
        dp = {}

        return helper(1, n)
