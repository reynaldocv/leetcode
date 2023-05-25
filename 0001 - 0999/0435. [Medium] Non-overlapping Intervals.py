# https://leetcode.com/problems/non-overlapping-intervals/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:      
        n = len(intervals)    
        
        intervals.sort(key = lambda item: (item[0], -item[1]))
        
        (s0, e0) = intervals[0]
        
        i = 1  
        
        ans = 0
        
        for i in range(1, n):
            (s1, e1) = intervals[i]
            
            sMax = max(s0, s1)
            eMin = min(e0, e1)     
            
            if sMax < eMin: 
                if e0 >= e1:                     
                    s0 = s1
                    e0 = e1  
                    
                ans += 1
                
            elif e0 < e1: 
                s0 = s1
                e0 = e1               
           
        return ans
                 
class Solution2:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        
        graph = defaultdict(lambda: [])
        
        start = inf 
        end = -inf
        
        dp = defaultdict(lambda: 0)
        
        for (a, b) in intervals: 
            graph[b].append(a)
            
            start = min(start, a)
            end = max(end, b)
            
        for i in range(start, end + 1):
            dp[i] = dp[i - 1]
            
            for x in graph[i]:
                dp[i] = max(dp[i], 1 + dp[x])
                
        return n - dp[end]
               
    
                
