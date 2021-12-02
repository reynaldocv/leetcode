# https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:        
        n = len(profits)
        
        arr = [(capital[i], profits[i]) for i in range(n)]
        arr.sort()
        
        profits = [p for (_, p) in arr]
        capital = [c for (c, _) in arr]
        
        i = 0
        heap = []
        
        for _ in range(k):
            while i < n and capital[i] <= w: 
                heappush(heap, -profits[i])
                i += 1
            
            if heap: 
                w += -heappop(heap)
                
        return w
        
        
