# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        
        for num in nums: 
            if num in seen: 
                return num 
            
            seen.add(num)
            
