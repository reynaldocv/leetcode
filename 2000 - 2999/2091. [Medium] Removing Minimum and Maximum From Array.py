# https://leetcode.com/problems/removing-minimum-and-maximum-from-array/

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        
        minElem = inf 
        maxElem = -inf
        
        index = {}
        
        for (ith, num) in enumerate(nums):
            minElem = min(minElem, num)
            maxElem = max(maxElem, num)
            
            index[num] = ith
            
        minIdx = min(index[minElem], index[maxElem])
        maxIdx = max(index[minElem], index[maxElem])
        
        return min(maxIdx + 1, n - minIdx, minIdx + 1 + n - maxIdx)
        
