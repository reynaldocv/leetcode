# https://leetcode.com/problems/find-the-losers-of-the-circular-game/

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        person = 0
        
        seen = set()
        
        steps = k 
        
        while person not in seen:
            seen.add(person)
            
            person = (person + steps) % n 
            steps = (steps + k) % n 
        
        return [i + 1 for i in range(n) if i not in seen]
        
            
        
