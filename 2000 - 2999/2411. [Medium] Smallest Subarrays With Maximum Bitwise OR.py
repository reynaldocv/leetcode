# https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        ans = [0 for i in range(n)]
        
        seen = [0 for i in range(30)]
        
        for i in range(n - 1, -1, -1): 
            for j in range(30): 
                if (nums[i] >> j) & 1 == 1: 
                    seen[j] = i 
            
            ans[i] = max(1, max(seen) - i + 1)
            
        return ans 
