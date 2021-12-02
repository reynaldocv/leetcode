# https://leetcode.com/problems/count-nice-pairs-in-an-array/

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        count = {}
        n = len(nums)
        ans = 0
        MOD = 10**9 + 7
        
        for i in range(n):
            delta = nums[i] - int(str(nums[i])[::-1])
            if delta in count: 
                ans += count[delta]
            count[delta] = count.get(delta, 0) + 1
        
        return ans % MOD
