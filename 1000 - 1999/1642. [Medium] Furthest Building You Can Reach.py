# https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        i = 0 
        heap = []
        while i < n - 1:            
            diff = heights[i + 1] - heights[i]
            if diff > 0:            
                bricks -= diff
                heappush(heap, -diff)
                if bricks < 0: 
                    if ladders:                        
                        bricks -= heappop(heap)
                        ladders -= 1
                    else: 
                        return i
            i += 1
            
        return i 
