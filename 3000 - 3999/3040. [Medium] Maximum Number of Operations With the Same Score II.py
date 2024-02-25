# https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        @cache 
        def helper(aSum, start, end):
            if start >= end: 
                return 0 
                
            else:
                ans = 0 
                
                if nums[start] + nums[start + 1] == aSum: 
                    ans = max(ans, 1 + helper(aSum, start + 2, end))
                
                if nums[start] + nums[end] == aSum: 
                    ans = max(ans, 1 + helper(aSum, start + 1, end - 1))
                    
                if nums[end] + nums[end - 1] == aSum: 
                    ans = max(ans, 1 + helper(aSum, start, end - 2))
                    
                return ans 
            
        n = len(nums)
        
        ans = 0 
        
        ans = max(ans, helper(nums[0] + nums[1], 0, n - 1))
        ans = max(ans, helper(nums[0] + nums[-1], 0, n - 1))
        ans = max(ans, helper(nums[-1] + nums[-2], 0, n - 1))
        
        return ans 
            
        
