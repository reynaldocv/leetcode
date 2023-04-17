# https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda item: (-item[0], item[1]))
        
        (maxAttack, maxDefense) = properties[0]
        
        ans = 0 
        
        for (attack, defense) in properties[1: ]: 
            if attack < maxAttack and defense < maxDefense:
                ans +=1 
                
            maxDefense = max(maxDefense, defense)
            
        return ans 
            
        
