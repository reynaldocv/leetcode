# https://leetcode.com/problems/sum-of-subarray-ranges/

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        
        ans = 0 
        
        for i in range(n):
            minElem = nums[i]
            maxElem = nums[i]
            
            for j in range(i + 1, n):
                minElem = min(minElem, nums[j])
                maxElem = max(maxElem, nums[j])
                
                ans += maxElem - minElem 
                
        return ans 
        
        
