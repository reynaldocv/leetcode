# https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        
        start = 1
        end = n 
        
        while end - start > 1: 
            mid = (end + start)//2
            
            if mid*(mid + 1)//2 <= n: 
                start = mid 
                
            else: 
                end = mid 
                
        return start
