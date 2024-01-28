# https://leetcode.com/problems/find-if-array-can-be-sorted/

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        @cache 
        def helper(number):
            ans = 0 
            
            while number: 
                bit = number & 1 
                
                if bit == 1: 
                    ans += 1 
                    
                number //= 2 
                
            return ans 
        
        n = len(nums)
        
        prev = 0 
        start = 0 
        
        for (i, num) in enumerate(nums + [0]): 
            if prev != helper(num):
                nums[start: i] = sorted(nums[start: i])
                
                start = i
                
            prev = helper(num)
            
        return nums == sorted(nums)
            
                
                
        
        
        
