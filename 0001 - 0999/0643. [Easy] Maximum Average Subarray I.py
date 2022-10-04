# https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        aSum = 0 
        
        for i in range(k):
            aSum += nums[i]
            
        ans = aSum/k 
        
        for (i, num) in enumerate(nums[k: ]):            
            aSum += num - nums[i]
            
            ans = max(ans, aSum/k)
            
        return ans 
        
