# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        def helper(arr):
            cnt = 0         
            prev = -inf 
            
            ans = 0

            for num in arr:
                if prev < num:
                    cnt += 1
                    
                else: 
                    cnt = 1 
                    
                ans = max(ans, cnt)
                prev = num
                
            return ans 
        
        return max(helper(nums), helper(nums[:: -1]))

            
        
