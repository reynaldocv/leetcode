https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        aSum = sum(nums)
        
        if aSum % 2 == 1: 
            return False 
        
        limit = aSum//2
        
        dp = [True] + [False for _ in range(limit)]
        
        for num in nums: 
            for end in range(limit, num - 1, -1):
                if dp[end - num] == True:
                    dp[end] = dp[end - num]
            
        return dp[-1]
        
        
    
