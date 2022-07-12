# https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        heap = []
        
        for a in amount: 
            if a != 0:
                heappush(heap, -a)
                
        ans = 0         
        
        while heap:
            if len(heap) >= 2: 
                a = -heappop(heap)
                b = -heappop(heap)                
                if a - 1 != 0:
                    heappush(heap, -(a - 1))                
                if b - 1 != 0:
                    heappush(heap, -(b - 1))
                
                ans += 1                 
            else:
                a = -heappop(heap)                
                ans += a 
                
        return ans 
