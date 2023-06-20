# https://leetcode.com/problems/find-the-value-of-the-partition/

class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        n = len(nums)
        
        nums.sort() 
        
        ans = inf 
        
        for i in range(n - 1):
            ans = min(ans, nums[i + 1] - nums[i])
            
        return ans 
        
