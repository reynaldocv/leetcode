# https://leetcode.com/problems/maximum-ascending-subarray-sum/

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = aux = nums[0]
        n = len(nums)
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                aux += nums[i]
            else: 
                aux = nums[i]
            ans = max(aux, ans)
        
        return ans
            
                
        
            
        
