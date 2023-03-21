# https://leetcode.com/problems/number-of-zero-filled-subarrays/

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0 
        
        ans = 0 
        
        for num in nums + [1]:
            if num == 0:                
                count += 1 
                
                ans += count
                
            else: 
                count = 0
                
        return ans 
