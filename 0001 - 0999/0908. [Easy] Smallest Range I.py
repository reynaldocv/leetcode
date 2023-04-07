# https://leetcode.com/problems/smallest-range-i/

ass Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        maxElem = max(nums)
        minElem = min(nums)
        
        if maxElem - minElem <= 2*k: 
            return 0 
        
        else: 
            return maxElem - minElem -2*k
        
        
        
        
        
