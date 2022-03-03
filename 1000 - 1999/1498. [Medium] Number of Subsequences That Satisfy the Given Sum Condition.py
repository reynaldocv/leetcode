# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        ans = 0 
        for (i, num) in enumerate(nums):
            if num <= target // 2: 
                idx = bisect_right(nums, target - num)
                if idx > i: 
                    ans += 1 + 2**(idx - i - 1) - 1      
                    ans %= MOD
            else: 
                break
            
        return ans % MOD
