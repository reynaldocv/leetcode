# https://leetcode.com/problems/array-partition-i/

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        
        nums.sort() 
        
        ans = 0 
        
        for i in range(0, n, 2):
            ans += min(nums[i], nums[i + 1])
            
        return ans 
        
        
