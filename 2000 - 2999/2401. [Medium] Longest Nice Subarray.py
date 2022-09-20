# https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans = 1
        seen = {}
        
        start = 0 
        
        for (idx, num) in enumerate(nums):
            for i in range(32):
                if (num >> i) & 1: 
                    if i not in seen: 
                        seen[i] = idx
                    else: 
                        start = max(start, seen[i] + 1)
                        seen[i] = idx
            
            ans = max(ans, idx - start + 1)
            
        return ans 
