# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        def helper(p, q):
            seen.add((p, q))
            
            x, y = p, q
            
            while x - 1 >= 0 and (x - 1, y) not in walls and (x - 1, y) not in guards: 
                seen.add((x - 1, y))
                x -= 1 
            
            x, y = p, q
            
            while x + 1 < m and (x + 1, y) not in walls and (x + 1, y) not in guards: 
                seen.add((x + 1, y))            
                x += 1 
                
            x, y = p, q
            
            while y - 1 >= 0 and (x, y - 1) not in walls and (x, y - 1) not in guards: 
                seen.add((x, y - 1))            
                y -= 1 
            
            x, y = p, q
            
            while y + 1 < n and (x, y + 1) not in walls and (x, y + 1) not in guards: 
                seen.add((x, y + 1))            
                y += 1 
            
        guards = {(a, b) for (a, b) in guards}
        walls = {(a, b) for (a, b) in walls}
        
        seen = set()
        
        for i in range(m):
            for j in range(n):
                if (i, j) in guards: 
                    helper(i, j)
                    
                    
        return m*n - len(seen) - len(walls)
                    
                    
    
                    
        
