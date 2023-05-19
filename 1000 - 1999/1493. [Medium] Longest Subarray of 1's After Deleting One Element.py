# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        def helper(arr):
            ans = [0 for _ in range(n)]
            
            cnt = 0 
            
            for (i, num) in enumerate(arr): 
                if num == 1:
                    cnt += 1 
                    
                else: 
                    cnt = 0 
                    
                ans[i] = cnt
                    
            return ans 
        
        n = len(nums)
        
        prefix = helper(nums)
        suffix = helper(nums[:: -1])[:: -1]
        
        ans = 0
        
        for i in range(n):
            left = prefix[i - 1] if i - 1 >= 0 else 0 
            right = suffix[i + 1] if i + 1 < n else 0 
            
            ans = max(ans, left + right)
            
        return ans 
            
            
            
                
        
                
               
