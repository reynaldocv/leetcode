# https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def helper(val):
            ans = 0 
            for num in nums: 
                if num > val: 
                    ans += (num - 1)//val 
                
            return ans 
        
        start = 0 
        end = max(nums) + 1
        
        while end -  start > 1: 
            m = (end + start)//2
            if helper(m) <= maxOperations: 
                end = m 
            else: 
                start = m
                
        return end
        
        
