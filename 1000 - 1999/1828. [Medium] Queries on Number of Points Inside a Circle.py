# https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        
        for (x, y, r) in queries: 
            counter = 0 
            
            for (p, q) in points: 
                if (x - p)**2 + (y - q)**2 <= r**2:
                    counter += 1 
            
            ans.append(counter)
            
        return ans 
            
        
                
        
        
        
