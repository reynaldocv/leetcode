# https://leetcode.com/problems/maximum-number-of-eaten-apples/

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)
        limit = max(i + days[i] for i in range(n))
        heap = []
        ans = 0 
        for i in range(limit + 1):
            if i < n and apples[i] > 0:                 
                heappush(heap, (i + days[i] - 1, apples[i]))
            
            while heap and heap[0][0] < i: 
                heappop(heap)
                
            if heap: 
                ans += 1
                (lastDay, numberApples) = heappop(heap)
                if numberApples > 1: 
                    heappush(heap, (lastDay, numberApples - 1))
                
        return ans 
            
                     
            
            
