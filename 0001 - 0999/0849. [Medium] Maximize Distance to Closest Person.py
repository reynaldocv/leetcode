# https://leetcode.com/problems/maximize-distance-to-closest-person/

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        
        occupied = [i for (i, num) in enumerate(seats) if num == 1]        
        m = len(occupied)
        
        ans = occupied[0]
        
        for i in range(m):
            left = occupied[i]
            
            if i == m - 1: 
                right = 2*n - 2 - occupied[-1]
            else:
                right = occupied[i + 1]
            
            if (right - left)//2 > ans:               
                ans = (right - left)//2
                
        return ans
    
        
                
        
        
        
