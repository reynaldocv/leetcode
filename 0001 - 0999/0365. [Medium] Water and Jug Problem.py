# https://leetcode.com/problems/water-and-jug-problem/

class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        mcd = gcd(jug1Capacity, jug2Capacity)
        
        return jug1Capacity + jug2Capacity >= targetCapacity and targetCapacity % mcd == 0
        
