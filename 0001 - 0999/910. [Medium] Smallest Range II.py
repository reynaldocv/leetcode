# https://leetcode.com/problems/smallest-range-ii/

class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        nums.sort()
        
        maxElem, minElem = nums[~0], nums[0]
        
        ans = maxElem - minElem
        
        for i in range(n - 1):
            newMax = nums[i] + k
            newMin = nums[i + 1] - k
            ans = min(ans, max(maxElem - k, newMax) - min(minElem + k, newMin))
            
        return ans
        
        
        
