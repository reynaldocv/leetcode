# https://leetcode.com/problems/find-the-maximum-divisibility-score/

class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        ans = (-1, -1)
        
        for divisor in divisors: 
            counter = 0 
            
            for num in nums:             
                if num % divisor == 0: 
                    counter += 1 
                    
            ans = max(ans, (counter, -divisor))
            
        return -ans[1]
                
        
