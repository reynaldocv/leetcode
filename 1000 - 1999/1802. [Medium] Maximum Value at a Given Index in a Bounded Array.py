# https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def helper(idx, val):
            if idx < 0: 
                return 0 
            
            ans = val*(val + 1)//2
            left = (val - idx - 1)
            
            if left > 0:                 
                ans -= left*(left + 1)//2
                
            return ans
        
        end = maxSum + 1
        start = 0
        maxSum -= n
        
        while end - start > 1:             
            m = (end + start)//2 
            if helper(index, m) + helper(n - index - 2, m - 1) <= maxSum: 
                start = m
            else:
                end = m 
            
        return start + 1
        
