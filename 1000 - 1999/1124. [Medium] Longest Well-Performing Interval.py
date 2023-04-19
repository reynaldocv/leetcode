# https://leetcode.com/problems/longest-well-performing-interval/

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        arr = [1 if hour > 8 else -1 for hour in hours]
        
        seen = {0: -1}        
        prev = 0 
        
        ans = 0
        
        for (i, hour) in enumerate(arr): 
            prev += hour 
            if prev > 0: 
                ans = max(ans, i + 1)
            
            if prev - 1 in seen:             
                ans = max(ans, i - seen[prev - 1])
                
            if prev not in seen: 
                seen[prev] = i 
                
        return ans 
            
        
