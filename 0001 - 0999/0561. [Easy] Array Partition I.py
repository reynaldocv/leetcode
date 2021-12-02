# https://leetcode.com/problems/array-partition-i/

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        ans = 0
        l = len(nums)//2
        nums.sort(reverse = True)
        for i in range(l):
            ans += nums[2*i + 1]
        return ans
        
