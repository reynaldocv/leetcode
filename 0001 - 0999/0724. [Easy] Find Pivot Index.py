# https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:     
        sumLeft = 0
        sumRight = sum(nums)
        n = len(nums)
        for i in range(n):
            if i - 1 >= 0:
                sumLeft += nums[i - 1]
            sumRight -= nums[i]
            if sumLeft == sumRight:
                return i
        return -1

        
