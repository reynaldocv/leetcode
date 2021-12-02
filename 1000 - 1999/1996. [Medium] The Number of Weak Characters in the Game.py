# https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        ans = 0 
        properties.sort(reverse = True, key = lambda item: (item[0], -item[1]))
        maxDef = -inf
        for (attack, defense) in properties:
            if defense < maxDef: 
                ans += 1
            else: 
                maxDef = defense
        
        return ans
        
        
