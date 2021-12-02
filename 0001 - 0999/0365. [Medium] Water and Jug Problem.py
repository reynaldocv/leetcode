# https://leetcode.com/problems/water-and-jug-problem/

class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if targetCapacity == 0: 
            return True
                
        if targetCapacity <= jug1Capacity + jug2Capacity: 
            return targetCapacity % gcd(jug1Capacity, jug2Capacity) == 0
    
        return False
