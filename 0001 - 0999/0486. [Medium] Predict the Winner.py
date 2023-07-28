# https://leetcode.com/problems/predict-the-winner/

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def helper(start, end):
            if start == end: 
                return nums[start]
            
            else: 
                ans = nums[start] - helper(start + 1, end)
                ans = max(ans, nums[end] - helper(start, end - 1))
                
                return ans 
        
        n = len(nums)
        
        return helper(0, n - 1) >= 0
