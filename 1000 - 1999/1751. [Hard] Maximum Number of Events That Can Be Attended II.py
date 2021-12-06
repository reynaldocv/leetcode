

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        @cache
        def dp(i, k):
            if k == 0 or i >= len(events):
                return 0
            
            idx = bisect.bisect_right(starts, events[i][1])
            
            val1 = events[i][-1] + dp(idx, k - 1)
            val2 = dp(i + 1, k)
            
            return max(val1, val2)
            
        events.sort() 
        starts = [x for (x, _, _) in events]
        
        return dp(0, k)
        
