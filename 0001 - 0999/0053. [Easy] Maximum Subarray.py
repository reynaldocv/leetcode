# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        aux, n, ans = 0, len(nums), -inf
        for i in range(n):
            aux = max(aux + nums[i], nums[i])
            ans = max(aux, ans)
            
        return ans
            
            
        
