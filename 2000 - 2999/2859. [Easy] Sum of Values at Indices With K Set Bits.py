# https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        def helper(number):
            ans = 0 
            
            while number > 0: 
                ans += number % 2
                
                number //= 2 
                
            return ans 
        
        ans = 0 
        
        for (i, num) in enumerate(nums):
            if helper(i) == k: 
                ans += num 
                
        return ans 
                
                
        
