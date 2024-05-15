# https://leetcode.com/problems/two-best-non-overlapping-events/

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        arr = [-1]
        dp = [0]
        
        ans = 0 
        
        events.sort(key = lambda item: item[1])
        
        for (start, end, value) in events: 
            idx = bisect_right(arr, start - 1) - 1
            
            ans = max(ans, dp[idx] + value)
            
            arr.append(end)
            dp.append(max(dp[-1], value))
            
        return ans 
        
            
        
        
