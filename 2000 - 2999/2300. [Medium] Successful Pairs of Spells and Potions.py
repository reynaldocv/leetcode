# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(potions)
        potions.sort()
        
        ans = []
        
        for spell in spells: 
            tmp = int(success/spell)
            
            if tmp != success/spell: 
                tmp += 1 
            
            idx = bisect_left(potions, tmp)
            
            ans.append(n - idx)
            
        return ans 
        
