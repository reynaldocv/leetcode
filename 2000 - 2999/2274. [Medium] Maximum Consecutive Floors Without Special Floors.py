# https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/
class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.extend([0, inf])
        
        n = len(special)
        
        special.sort() 
        
        ans = 0 
        
        for i in range(1, n):
            start = special[i - 1] + 1
            end = special[i] - 1
            
            if end >= start:
                maxStart = max(start, bottom)
                minEnd = min(end, top)
                
                if maxStart <= minEnd: 
                    ans = max(ans, minEnd - maxStart + 1)
                    
        return ans 
        
        
