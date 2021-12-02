https://leetcode.com/problems/rotate-function/

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        
        value = 0 
        for (i, num) in enumerate(nums):
            value += i*num
        
        ans = value
        aSum = sum(nums)
        n = len(nums)
        
        for i in range(n - 1, 0, -1):
            value = value + aSum - n*nums[i]
            ans = max(ans, value)
            
        return ans
        
