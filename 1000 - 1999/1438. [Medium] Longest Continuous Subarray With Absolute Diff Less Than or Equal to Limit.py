# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        arr = [nums[0]]
        ans = 1
        
        i = 0 
        for num in nums[1: ]: 
            insort(arr, num)
            while arr[-1] - arr[0] > limit: 
                idx = bisect_left(arr, nums[i])
                arr.pop(idx)
                i += 1
                
            ans = max(ans, len(arr))
            
        return ans
                
            
                      
