# https://leetcode.com/problems/valid-mountain-array/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        def helper(nums):
            n = len(nums)
            
            ans = -1
            
            for i in range(1, n):
                if nums[i - 1] < nums[i]:
                    ans = i 
                    
                else: 
                    break 
                    
            return ans 
        
        n = len(arr)
        
        left = helper(arr)
        right = helper(arr[:: -1])
        
        if left == -1 or right == -1: 
            return False 
        
        return left == n - right - 1
        
