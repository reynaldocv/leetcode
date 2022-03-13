# https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/

class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        if n == 1 and k & 1 == 1:
            return -1
        
        ans = 0 
        
        for i in range(min(k - 1, n)):
            ans = max(ans, nums[i])
            
        if k < n: 
            ans = max(ans, nums[k])
        
        return ans
