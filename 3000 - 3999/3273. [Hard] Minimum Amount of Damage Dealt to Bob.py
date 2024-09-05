# https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/

class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        n = len(damage)
        
        attacks = []
        heap = []
        
        for (ith, h) in enumerate(health): 
            attacks.append(ceil(h/power))
            
            heappush(heap, (-damage[ith]/attacks[ith], damage[ith], ith))
            
        totalDamage = sum(damage)
        
        ans = 0 
        
        while heap: 
            (_, damage, ith) = heappop(heap)
            
            ans += totalDamage*attacks[ith]
            
            totalDamage -= damage
            
        return ans 
        
            
