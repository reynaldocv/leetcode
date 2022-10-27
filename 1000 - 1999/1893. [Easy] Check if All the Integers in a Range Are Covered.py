# https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        limit = right
        for (a, b) in ranges: 
            limit = max(limit, b)
        
        
        seen = [0 for i in range(limit + 1)]
        
        for (a, b) in ranges: 
            for x in range(a, b + 1):
                seen[x] += 1 
                
        for x in range(left, right + 1):
            if seen[x] == 0: 
                return False 
            
        return True 
                
        
