# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(potions)
        
        potions.sort()
        
        ans = []
        
        for spell in spells: 
            ratio = success//spell
            
            if success % spell != 0: 
                ratio += 1 
                
            idx = bisect_left(potions, ratio)
            
            ans.append(n - idx)
            
        return ans 
        
