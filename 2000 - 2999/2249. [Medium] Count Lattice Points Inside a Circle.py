# https://leetcode.com/problems/count-lattice-points-inside-a-circle/

class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        ans = 0 
        
        seen = set([])
        
        for (p, q, r) in circles: 
            for x in range(p - r, p + r + 1):
                for y in range(q - r, q + r + 1):
                    if (x, y) not in seen: 
                        if (x - p)**2 + (y - q)**2 <= r**2:
                            seen.add((x, y))
                            
                            ans += 1 
                            
        return ans 
        
