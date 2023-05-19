# https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = len(nums) 
        
        nums.sort() 
        
        start = 0 
        end = n - 1
        
        ans = 0 
        
        while end - start > 0: 
            tmp = nums[start] + nums[end]
            if tmp == k: 
                ans += 1 
                
                start += 1 
                end -= 1 
                
            elif tmp < k: 
                start += 1 
                
            else: 
                end -= 1 
                
        return ans 
                
    
            
