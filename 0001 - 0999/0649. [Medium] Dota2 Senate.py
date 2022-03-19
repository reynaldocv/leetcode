# https://leetcode.com/problems/dota2-senate/

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant, dire = [], []
        for (i, man) in enumerate(senate):
            if man == "R":
                radiant.append(i)
            else: 
                dire.append(i)
                
        n = len(senate)        
        
        while radiant and dire: 
            if radiant[0] < dire[0]:
                radiant.append(radiant.pop(0) + n)
                dire.pop(0)                
            else: 
                radiant.pop(0)
                dire.append(dire.pop(0) + n)
                
        return "Radiant" if radiant else "Dire"
