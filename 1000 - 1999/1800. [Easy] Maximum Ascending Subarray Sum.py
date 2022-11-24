# https://leetcode.com/problems/maximum-ascending-subarray-sum/

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:      
        prev = -inf
        aSum = 0 
        
        ans = 0 
        
        for num in nums: 
            if prev < num: 
                aSum += num                
                
            else: 
                aSum = num 
                
            prev = num 
            ans = max(ans, aSum)
                
        return ans 
            
            
        

        
            
                
        
            
        
