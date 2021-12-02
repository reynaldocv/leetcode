# https://leetcode.com/problems/find-the-middle-index-in-array/

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        rightSum = sum(nums)
        leftSum = 0 
        n = len(nums)
        for i in range(n):
            rightSum -= nums[i]
            if rightSum == leftSum: 
                return i
            leftSum += nums[i]
        
        return -1
        
        
