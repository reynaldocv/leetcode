# https://leetcode.com/problems/sum-of-subarray-ranges/

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0 
        n = len(nums)
        for i in range(n):
            maxElem = minElem = nums[i]
            for j in range(i + 1, n):
                maxElem = max(maxElem, nums[j])
                minElem = min(minElem, nums[j])
                ans += abs(maxElem - minElem)
                
        return ans
        
        
