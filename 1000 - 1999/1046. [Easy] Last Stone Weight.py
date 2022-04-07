# https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones: 
            heappush(heap, -stone)
            
        while len(heap) >= 2: 
            stone1 = -heappop(heap)
            stone2 = -heappop(heap)
            if stone1 != stone2: 
                stone3 = abs(stone1 - stone2)
                heappush(heap, -stone3)
                
        return -heappop(heap) if heap else 0 
        
