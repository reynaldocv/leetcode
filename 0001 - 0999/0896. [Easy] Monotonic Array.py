# https://leetcode.com/problems/monotonic-array/

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        def helper(arr):
            for i in range(n - 1):
                if arr[i] > arr[i + 1]:
                    return False 
                
            return True 
        
        n = len(nums)
        
        return helper(nums) or helper(nums[:: -1])
        
                
        
                
 
