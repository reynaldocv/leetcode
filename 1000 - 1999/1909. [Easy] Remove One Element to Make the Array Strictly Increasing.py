# https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        nums = [-inf] + nums + [inf]
        
        n = len(nums)
        
        left = [True] + [False for i in range(n - 1)]
        
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                left[i] = True
                    
            else: 
                break 
                
        right = [False for i in range(n - 1)] + [True]
        
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                right[i] = True
                
            else: 
                break 
                
        for i in range(1, n - 1):
            if nums[i - 1] < nums[i + 1] and left[i - 1] and right[i + 1]:
                return True 
            
        return False 
        
        
    
