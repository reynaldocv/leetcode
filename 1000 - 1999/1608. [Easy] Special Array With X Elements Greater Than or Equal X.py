# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        def helper(value):
            ans = 0 
            for num in nums: 
                if num >= value: 
                    ans += 1 
                    
            return ans 
        
        start = 0 
        end = max(nums) + 1
        
        while end - start > 1: 
            mid = (end + start)//2 
            if helper(mid) == mid: 
                return mid
            elif helper(mid) < mid: 
                end = mid
            else: 
                start = mid 
                
        return -1
                    
                    
