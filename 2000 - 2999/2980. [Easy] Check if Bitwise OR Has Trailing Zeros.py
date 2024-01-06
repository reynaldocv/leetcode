# https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/

class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        count = 0 
        
        for num in nums: 
            if num % 2 == 0: 
                count += 1 
                
        return count >= 2 
        
