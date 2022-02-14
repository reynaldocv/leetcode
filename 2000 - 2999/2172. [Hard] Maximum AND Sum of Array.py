# https://leetcode.com/problems/maximum-and-sum-of-array/

class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        @cache
        def helper(k, m):
            if k == n: 
                return 0 
            else: 
                ans = 0 
                for i in range(numSlots):
                    if m & (1 << 2*i) == 0 or m & (1 << 2*i + 1) == 0:
                        if m & 1 << 2*i == 0: 
                            mm = m ^ 1 << 2*i
                        else: 
                            mm = m ^ 1 << 2*i + 1
                        ans = max(ans, (nums[k] & i + 1) + helper(k + 1, mm))
                
                return ans
            
        n = len(nums)
        
        return helper(0, 0)
