# https://leetcode.com/problems/removing-minimum-and-maximum-from-array/

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)        
        maxIdx = nums.index(max(nums))
        minIdx = nums.index(min(nums))
        
        ans = 0 
        
        val1 = max(minIdx, maxIdx) + 1
        val2 = max(n - minIdx, n - maxIdx)
        val3 = min(minIdx, maxIdx) + 1 + n - max(minIdx, maxIdx)
        
        return min(val1, val2, val3)  
