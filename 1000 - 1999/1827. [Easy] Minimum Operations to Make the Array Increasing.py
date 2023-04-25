# https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums) 
        
        last = nums[0] + 1
        
        ans = 0 
        
        for i in range(1, n):
            if last > nums[i]:
                ans += last - nums[i]
                
                last += 1
                
            else: 
                last = nums[i] + 1
                
        return ans
                
