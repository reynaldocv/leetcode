# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prev = 0 
        
        ans = inf 
        
        for num in nums: 
            prev += num 
            
            ans = min(ans, prev)
            
        if ans <= 0: 
            return -ans + 1
    
        else: 
            return 1
            
