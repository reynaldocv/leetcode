# https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def helper(value):  
            left = max(0, value - index - 1) 
            right = max(0, value - (n - 1 - index) - 1)
            
            tmp = collaborator(left, value)
            tmp += collaborator(right, value)
            
            return tmp - value <= maxSum
            
        def collaborator(start, end):
            return end*(end + 1)//2 - start*(start + 1)//2
            
        start = 0 
        end = maxSum + 1 
        
        maxSum -= n 
        
        while end - start > 1: 
            middle = (end + start)//2
            
            if helper(middle):
                start = middle 
                
            else: 
                end = middle
                
        return start + 1
            
        
