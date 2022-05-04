# https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = len(nums) 
        
        nums.sort() 
        
        ans = 0 
        
        start = 0 
        end = n - 1
        
        while end > start: 
            if nums[start] + nums[end] == k:
                ans += 1 
                start += 1 
                end -= 1 
                
            elif nums[start] + nums[end] < k:
                start += 1 
            
            else: 
                end -= 1 
                
        return ans 
    
            
