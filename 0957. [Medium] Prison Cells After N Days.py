# https://leetcode.com/problems/prison-cells-after-n-days/

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        start = tuple(cells)
        seen = {}        
        day = 0 
        cycle = []
        
        while start not in seen: 
            seen[start] = day
            cycle.append(start)
            
            aux = [0 for i in range(8)]
            for i in range(1, 7):
                aux[i] = 1 if start[i - 1] == start[i + 1] else 0 
                
            start = tuple(aux)
                       
            if day + 1 == n: 
                return start
              
            day += 1
            
        n -= seen[start]
        cycle = cycle[seen[start]: ]
        
        m = len(cycle)
        n = n % m 
        
        return cycle[n]
