https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = sum(nums)
        
        if _sum % 2 == 1: 
            return False
        
        target = _sum//2
        n = len(nums)
        dp = [False for i in range(target + 1)]
        dp[0] = True
        
        for i in range(n):
            newDp = list(dp)                
            for t in range(nums[i], target + 1):
                if 0 <= t - nums[i] <= target: 
                    newDp[t] = dp[t] or dp[t - nums[i]]
                    
            dp = newDp
            
        return dp[-1]
        
    
