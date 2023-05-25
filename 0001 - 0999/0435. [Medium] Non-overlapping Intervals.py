# https://leetcode.com/problems/non-overlapping-intervals/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:      
        n = len(intervals)    
        
        intervals.sort(key = lambda item: (item[0], -item[1]))
        
        (start0, end0) = intervals[0]
        
        ans = 0
        
        for i in range(1, n):
            (start1, end1) = intervals[i]
            
            maxStart = max(start0, start1)
            minEnd = min(end0, end1)     
            
            if maxStart < minEnd: 
                if end0 >= end1:                     
                    (start0, end0) = (start1, end1)
                    
                ans += 1
                
            else: 
                (start0, end0) = (start1, end1)
                    
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
               
    
                
