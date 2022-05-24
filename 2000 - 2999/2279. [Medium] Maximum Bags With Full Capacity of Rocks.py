# https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        
        heap = []
        
        for i in range(n):                        
            capacity[i] -= rocks[i]
            heappush(heap, capacity[i])
            
        ans = 0 
        
        while heap and additionalRocks > 0: 
            value = heappop(heap)
            if value <= additionalRocks: 
                ans += 1 
                additionalRocks -= value
                
        return ans 
