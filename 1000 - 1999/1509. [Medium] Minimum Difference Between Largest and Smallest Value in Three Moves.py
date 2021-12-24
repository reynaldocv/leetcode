# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n <= 4: 
            return 0 
        
        nums.sort()
        
        ans = inf
        for i in range(4):
            ans = min(ans, nums[-(4 - i)] - nums[i])
        
        return ans
