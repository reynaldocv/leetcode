# https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/

class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        n = len(nums)
        
        start = 0 
        end = n - 1
        
        while start < n and nums[start] == 0: 
            start += 1 
            
        while end >= 0 and nums[end] == 0: 
            end -= 1 
            
        if end < start: 
            return 0 
            
        ans = 1 
        
        cnt = 1
        
        for i in range(start, end + 1):
            if nums[i] == 1:
                if cnt > 0: 
                    ans = (ans * cnt) % MOD
                
                cnt = 1
                
            else: 
                cnt += 1 
                
        return ans 
        
