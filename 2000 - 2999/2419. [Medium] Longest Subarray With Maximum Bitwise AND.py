# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxElem = max(nums)
        
        ans = cnt = 0 
        
        for num in nums: 
            if num == maxElem: 
                cnt += 1 
                
            else: 
                cnt = 0 
                
            ans = max(ans, cnt)
            
        return ans 
                
                
