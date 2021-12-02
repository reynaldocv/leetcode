# https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        aSum = tank = 0
        start = 0
        for i in range(n):
            tank += gas[i] - cost[i]
            aSum += gas[i] - cost[i]
            if tank < 0: 
                tank = 0
                start = i + 1
        
        return -1 if aSum < 0 else start
