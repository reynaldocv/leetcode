# https://leetcode.com/problems/minimum-size-subarray-sum/submissions/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = inf
        left = 0 
        aSum = 0 
        for i in range(n):
            aSum += nums[i]
            while aSum >= target: 
                ans = min(ans, i - left + 1)
                aSum -= nums[left]
                left += 1
                
        return ans if ans != inf else 0 
        
        
                
            
            
        
