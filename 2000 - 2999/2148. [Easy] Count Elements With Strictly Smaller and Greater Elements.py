# https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/

class Solution:
    def countElements(self, nums: List[int]) -> int:
        minElem = min(nums)
        maxElem = max(nums)
        
        ans = 0
        
        for num in nums: 
            if minElem < num < maxElem: 
                ans += 1 
                
        return ans
        
