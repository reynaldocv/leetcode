# https://leetcode.com/problems/product-of-array-except-self/ 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count0 = 0
        totalMul = 1
        n = len(nums)
        ans = [0]*n
        for num in nums: 
            count0 = count0 + 1 if num == 0 else count0
            totalMul = totalMul*num if num != 0 else totalMul
        
        if count0 < 2: 
            if count0 == 1: 
                for (i, num) in enumerate(nums):
                    if num == 0: 
                        ans[i] = totalMul
            else: 
                for (i, num) in enumerate(nums):
                    ans[i] = totalMul//num
        
        return ans
            
            
                    
        
