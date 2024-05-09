# https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def helper(value):
            ans = 0 
            
            for num in nums: 
                ans += (num - 1)//value 
                
            return ans 
        
        start = 0 
        end = max(nums)
        
        while end - start > 1: 
            mid = (end + start)//2
            
            if helper(mid) <= maxOperations: 
                end = mid 
                
            else: 
                start = mid 
                
        return end 
        
        
