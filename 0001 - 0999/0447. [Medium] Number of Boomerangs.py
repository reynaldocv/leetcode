# https://leetcode.com/problems/number-of-boomerangs/

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        
        ans = 0 
        
        for i in range(n):
            counter = defaultdict(lambda: 0)
        
            for j in range(n):
                (x0, y0) = points[i]
                (x1, y1) = points[j]
                
                distance = (x1 - x0)**2 + (y1 - y0)**2 
                
                counter[distance] += 1 
            
            for key in counter: 
                items = counter[key]
                
                ans += items*(items - 1)

        return ans 
                
                
        
                
                    
        
        
