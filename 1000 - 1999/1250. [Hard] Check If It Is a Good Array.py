# https://leetcode.com/problems/check-if-it-is-a-good-array/

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        mcd = nums[0]        
        
        for num in nums: 
            mcd = gcd(mcd, num)
            
            if mcd == 1: 
                return True 
            
        return False 
        
