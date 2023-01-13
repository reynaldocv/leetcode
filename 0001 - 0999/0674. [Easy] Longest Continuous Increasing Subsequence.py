# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums) 
        
        ans = cnt = 1 
        
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                cnt += 1 
                
            else: 
                cnt = 1 
                
            ans = max(ans, cnt)
                
        return ans 
        
        
        
