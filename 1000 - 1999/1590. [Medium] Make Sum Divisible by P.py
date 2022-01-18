# https://leetcode.com/problems/make-sum-divisible-by-p/

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        aSum = sum(nums)
        if aSum % p == 0: 
            return 0
        
        n = len(nums)
        prefix = 0 
        ans = inf
        last = {0: -1}
        
        for (i, num) in enumerate(nums):
            prefix = prefix + num
            right = aSum - prefix
            left = (p - right) % p
            if left in last:                 
                ans = min(ans, i - last[left])
                
            last[prefix % p] = i 
            
        return ans if (ans != n) else -1
            
            
            
