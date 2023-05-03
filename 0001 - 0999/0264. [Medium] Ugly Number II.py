# https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        seen = {1}
        
        for _ in range(n - 1):
            num = heappop(heap)
            
            for r in [2, 3, 5]:
                if r*num not in seen: 
                    heappush(heap, r*num)
                    
                    seen.add(r*num)
                    
        return heappop(heap)
                    
                    
        
