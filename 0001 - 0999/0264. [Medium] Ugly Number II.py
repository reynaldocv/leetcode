# https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        idx = 1
        heap = [1]
        seen = {1: True}
        while idx < n: 
            num = heappop(heap)
            for k in [2, 3, 5]:
                if k*num not in seen: 
                    heappush(heap, k*num)
                    seen[k*num] = True
            idx += 1
        
        return heappop(heap)
         
            
        
