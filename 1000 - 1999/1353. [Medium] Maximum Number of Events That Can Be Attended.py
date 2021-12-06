# 1353. Maximum Number of Events That Can Be Attended

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events = sorted(events)  
        
        last = max(y for (x, y) in events)
            
        ans = 0
        ith = 0
        heap = []
        
        for day in range(1, last + 1):            
            while ith < len(events) and events[ith][0] == day:
                heappush(heap, events[ith][1])
                ith += 1
            
            while heap and heap[0] < day:
                heappop(heap)
            
            if heap:
                heappop(heap)
                ans += 1
            
        return ans
            
            
