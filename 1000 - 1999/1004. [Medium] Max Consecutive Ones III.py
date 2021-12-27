# https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        seen = {-1: -1}
        idx = 0
        ans = 0 
        for (i, num) in enumerate(nums):
            if num == 0: 
                seen[idx] = i 
                idx += 1
            
            prev = idx - k - 1 if idx > k else -1            
            ans = max(ans, i - seen[prev])
            
        return ans
        
