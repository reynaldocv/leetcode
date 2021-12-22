# https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        val = 1
        
        for num in arr: 
            if num >= val: 
                val += 1
            
        return val - 1
            
                
        
