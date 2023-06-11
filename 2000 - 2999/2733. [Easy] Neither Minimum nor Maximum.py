# https://leetcode.com/problems/neither-minimum-nor-maximum/

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        minElem = inf 
        maxElem = -inf 
        
        for num in nums: 
            minElem = min(minElem, num)
            maxElem = max(maxElem, num)
            
        for num in nums: 
            if num != minElem and num != maxElem: 
                return num 
            
        return -1
        
