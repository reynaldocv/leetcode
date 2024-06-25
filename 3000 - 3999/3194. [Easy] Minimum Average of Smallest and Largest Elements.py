# https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        n = len(nums)
        
        ans = inf 
        
        nums.sort() 
        
        for i in range(n//2):
            tmp = (nums[i] + nums[n - 1 - i])/2
            
            ans = min(ans, tmp)
            
        return ans
            
            
        
