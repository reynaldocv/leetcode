# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        ans = 0 
        
        for i in range(n - 2):
            if nums[i] == 0: 
                nums[i] = 1 - nums[i] 
                
                nums[i + 1] = 1 - nums[i + 1]
                nums[i + 2] = 1 - nums[i + 2]
                
                ans += 1 
                
        if sum(nums) == n: 
            return ans
        
        else: 
            return -1 
        
        
