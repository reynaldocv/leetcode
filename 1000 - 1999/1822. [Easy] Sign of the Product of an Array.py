# https://leetcode.com/problems/sign-of-the-product-of-an-array/

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for num in nums:
            if num == 0: 
                ans = 0
                break
            elif num < 0:
                ans *= -1
        return ans
                
        
