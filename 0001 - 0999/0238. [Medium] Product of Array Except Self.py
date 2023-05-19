# https://leetcode.com/problems/product-of-array-except-self/ 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        
        counter = 0 
        
        mult = 1 
        
        ans = [0 for _ in range(n)]
        
        for num in nums: 
            if num == 0: 
                counter += 1 
            
            else: mult *= num 
                
        if counter == 1: 
            for (i, num) in enumerate(nums):
                if num == 0: 
                    ans[i] = mult
                    
        elif counter == 0:
            for (i, num) in enumerate(nums):
                ans[i] = mult//num
                
        return ans 
            
            
            
                    
        
