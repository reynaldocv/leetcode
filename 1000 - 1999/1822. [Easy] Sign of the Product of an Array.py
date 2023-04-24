# https://leetcode.com/problems/sign-of-the-product-of-an-array/

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        
        for num in nums: 
            if num > 0: 
                ans *= 1 
                
            elif num < 0: 
                ans *= -1
                
            else: 
                return 0 
            
        return ans 
        
        
