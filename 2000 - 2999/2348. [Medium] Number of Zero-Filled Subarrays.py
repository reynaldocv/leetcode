# https://leetcode.com/problems/number-of-zero-filled-subarrays/

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cnt = 0 
        ans = 0 
        
        for num in nums: 
            if num == 0: 
                cnt += 1
                ans += cnt 
                
            else: 
                cnt = 0 
            
        return ans 
            
                
