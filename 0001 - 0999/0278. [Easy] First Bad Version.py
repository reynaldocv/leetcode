# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 0 
        end = n 
        
        while end - start > 1: 
            mid = (end + start)//2
            
            if isBadVersion(mid): 
                end = mid 
            else: 
                start = mid 
                
        return end 
            
            
        
