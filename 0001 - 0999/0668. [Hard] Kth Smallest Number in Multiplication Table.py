# https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def helper(value):
            ans = 0 
            
            for i in range(1, m + 1):
                ans += min(n, value//i)   
                
            return ans 
        
        start = 0 
        end = m*n 
        
        while end - start > 1: 
            mid = (end + start)//2
            
            if helper(mid) < k: 
                start = mid 
                
            else: 
                end = mid
                
        return end 
        
            
        
