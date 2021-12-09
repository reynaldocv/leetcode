# https://leetcode.com/problems/longest-well-performing-interval/

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        arr = [1 if hour > 8 else - 1 for hour in hours]
        
        prev = 0 
        seen = {prev: -1}
        
        ans = 0 
        
        for (i, num) in enumerate(arr): 
            prev += num
            if prev - 1 in seen:
                ans = max(ans, i - seen[prev - 1])
                
            if prev > 0: 
                ans = max(ans, i + 1)
                
            if prev not in seen: 
                seen[prev] = i
            
        return ans
            
        
