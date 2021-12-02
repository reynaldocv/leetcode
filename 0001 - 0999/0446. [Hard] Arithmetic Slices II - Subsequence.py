# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        m = [{} for _ in range(n)]
        ans = 0 
        for i in range(1, n):
            for j in range(i):
                delta = nums[i] - nums[j]
                if delta not in m[j]: 
                    m[j][delta] = 0
                if delta not in m[i]: 
                    m[i][delta] = 0
                ans += m[j][delta]
                m[i][delta] += m[j][delta] + 1
        
        return ans
