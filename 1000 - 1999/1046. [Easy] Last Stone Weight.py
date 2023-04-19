# https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        
        for stone in stones: 
            heappush(heap, -stone)
            
        while len(heap) > 1: 
            stone1 = -heappop(heap)
            stone2 = -heappop(heap)
            
            remain = abs(stone1 - stone2)
            
            if remain != 0:             
                heappush(heap, -remain)
            
        if heap: 
            return -heappop(heap)
        
        return 0 
        
            
