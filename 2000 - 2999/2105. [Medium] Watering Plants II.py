# https://leetcode.com/problems/watering-plants-ii/

class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n = len(plants)
        canA = capacityA
        canB = capacityB
        
        ans = 0 
        
        for i in range(n//2):
            if canA >= plants[i]:
                canA -= plants[i]
            else: 
                canA = capacityA - plants[i]
                ans += 1
            
            if canB >= plants[~i]:
                canB -= plants[~i]
            else: 
                canB = capacityB - plants[~i]
                ans += 1
                
        if n % 2 == 1: 
            if max(canB, canA) < plants[n//2]:                 
                ans += 1
                
        return ans
            
        
