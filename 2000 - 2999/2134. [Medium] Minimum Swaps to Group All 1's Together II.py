# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        aSum = sum(nums)
        ans = 0 
        
        n = len(nums)
        
        nums = nums + nums
        aux = sum(nums[:aSum])
        
        for (i, bit) in enumerate(nums[aSum:n + aSum]):
            aux += bit
            aux -= nums[i]
            ans = max(ans, aux)
                
        return aSum - ans
      
