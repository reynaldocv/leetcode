# https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        aSum = 0 
        n = 0 
        
        for num in nums: 
            if num % 6 == 0: 
                aSum += num 
                n += 1 
        
        return aSum//n if n > 0 else 0 
