# https://leetcode.com/problems/number-of-boomerangs/

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for (i, (x0, y0)) in enumerate(points):
            seen = defaultdict(lambda: 0)
            for (j, (x1, y1)) in enumerate(points):
                if i != j:
                    dist = (y1 - y0)**2 + (x1 - x0)**2
                    seen[dist] += 1
            
            for key in seen: 
                ans += (seen[key] - 1)*(seen[key])
                
        return ans
                
                    
        
        
