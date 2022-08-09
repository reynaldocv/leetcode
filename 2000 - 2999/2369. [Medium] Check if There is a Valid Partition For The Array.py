# https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        
        nums = [1] + nums
        
        dp = [True] + [False for _ in range(n)]
        
        for i in range(2, n + 1):
            tmp = False 
            if i - 2 >= 0 and nums[i] == nums[i - 1]: 
                tmp = tmp or dp[i - 2] 
            
            if i - 3 >= 0 and nums[i] == nums[i - 1] and nums[i - 1] == nums[i - 2]: 
                tmp = tmp or dp[i - 3] 
                
            if i - 3 >= 0 and nums[i] - 1 == nums[i - 1] and nums[i - 1] - 1 == nums[i - 2]:
                tmp = tmp or dp[i - 3]
                
            dp[i] = tmp 
            
        return dp[-1]
