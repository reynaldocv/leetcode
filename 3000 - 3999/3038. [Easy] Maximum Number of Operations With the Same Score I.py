# https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-i/

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n < 2: 
            return 0 
        
        ans = 1
        
        prev = nums[0] + nums[1]
        
        for i in range(1, n//2):
            num = nums[2*i] + nums[2*i + 1]
            
            if num == prev: 
                ans += 1 
                
            else:                 
                break 
                
        return ans
            
        
