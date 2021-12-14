# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        
        right = [num for num in nums]
        
        for i in range(n - 1, -1, -1):
            if nums[i] == 1:
                right[i] += right[i + 1] if i + 1 < n else 0 
        
        ans = 0 
        prev = 0 
        
        for i in range(n):
            valR = right[i + 1] if i + 1 < n else 0                 
            ans = max(ans, prev + valR)
            
            prev = prev + 1 if nums[i] == 1 else 0 
                
        return ans
                
               
