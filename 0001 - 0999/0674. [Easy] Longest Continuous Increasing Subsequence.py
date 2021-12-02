# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        counter = 1
        n = len(nums)
        ans = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:                
                counter += 1                
            else:
                ans = max(ans, counter) 
                counter = 1
        return max(ans, counter)
            
        
