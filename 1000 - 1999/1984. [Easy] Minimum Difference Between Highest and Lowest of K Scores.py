# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1: 
            return 0 
        
        nums.sort() 
        
        n = len(nums)
        
        ans = inf
        
        for i in range(k - 1, n):
            ans = min(ans, nums[i] - nums[i - k + 1])
            
        return ans 
        
