# https://leetcode.com/problems/count-alternating-subarrays/

class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        prev = 1 - nums[0]        
        cnt = 0 
        
        ans = 0 
        
        for num in nums: 
            if prev != num: 
                cnt += 1 
                
            else: 
                cnt = 1 
            
            ans += cnt            
            prev = num 
            
        return ans 
        
