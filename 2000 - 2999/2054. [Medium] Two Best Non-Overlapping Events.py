# https://leetcode.com/problems/two-best-non-overlapping-events/

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        n = len(events)
        events.sort()            
        seen = {}
        aux = 0
        
        for i in range(n - 1, -1, -1):
            aux = max(aux, events[i][2])
            seen[events[i][0]] = aux
        
        keys = [*seen]
        keys.sort()
        
        ans = max([val for (_, _, val) in events])
            
        for i in range(n - 1): 
            idx = bisect_left(keys, events[i][1] + 1)
            if idx < len(keys):
                ans = max(ans, events[i][2] + seen[keys[idx]])
        
        return ans
            
            
        
        
