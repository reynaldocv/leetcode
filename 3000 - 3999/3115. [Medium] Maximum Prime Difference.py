# https://leetcode.com/problems/maximum-prime-difference/

class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def helper(number):
            if number == 1: 
                return False 
            
            if number == 2: 
                return True 
            
            if number % 2 == 0: 
                return False 
            
            limit = int(number**.5) + 2 
            
            for div in range(3, limit, 2):
                if number % div == 0: 
                    return False 
                
            return True 
        
        n = len(nums)
        
        left = 0 
        right = n - 1
        
        while left < n and helper(nums[left]) == False: 
            left += 1 
            
        while right >= 0 and helper(nums[right]) == False: 
            right -= 1 
            
        return right - left
        
