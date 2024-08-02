# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

class Solution:
    def minSwaps(self, nums: List[int]) -> int:     
        ones = sum(nums)
        
        ans = 0
        
        arr = nums + nums
        
        n = len(nums)
        
        counter = sum(arr[: ones])
        
        for (i, bit) in enumerate(arr[ones: ], 0):
            counter += bit
            counter -= arr[i]
            
            ans = max(ans, counter)
                
        return ones - ans
      
