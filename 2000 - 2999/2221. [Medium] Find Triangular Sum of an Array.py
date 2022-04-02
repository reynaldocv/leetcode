# https://leetcode.com/problems/find-triangular-sum-of-an-array/

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
                
        for i in range(n - 1, 0, -1):
            aux = nums.copy()
            for j in range(i):
                nums[j] = (aux[j] + aux[j + 1]) % 10 
                
        return nums[0]
