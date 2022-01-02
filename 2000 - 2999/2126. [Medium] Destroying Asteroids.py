# https://leetcode.com/problems/destroying-asteroids/

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        i = 0
        n = len(asteroids)
        
        while i < n and mass >= asteroids[i]:
            mass += asteroids[i]
            i += 1
            
        return i == n
        
        
