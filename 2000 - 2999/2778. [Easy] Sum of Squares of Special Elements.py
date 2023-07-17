# https://leetcode.com/problems/sum-of-squares-of-special-elements/

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums) 
        
        ans = 0 
        
        for (i, num) in enumerate(nums):
            if n % (i + 1) == 0: 
                ans += num**2

        return ans             
        
