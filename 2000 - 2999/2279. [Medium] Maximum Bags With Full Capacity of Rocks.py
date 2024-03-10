# https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity) 
        
        heap = []
        
        ans = 0 
        
        for i in range(n):
            diff = capacity[i] - rocks[i]
            
            heappush(heap, (diff))
                
        while heap and heap[0] <= additionalRocks: 
            additionalRocks -= heappop(heap)
            
            ans += 1 
            
        return ans 
        
        
