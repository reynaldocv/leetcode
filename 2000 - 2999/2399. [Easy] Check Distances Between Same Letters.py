# https://leetcode.com/problems/check-distances-between-same-letters/

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        seen = {}
        for (i, char) in enumerate(s): 
            if char not in seen: 
                seen[char] = i 
                
            else: 
                idx = ord(char) - ord("a")
                if i - seen[char] - 1 != distance[idx]: 
                    return False 
                
        return True 
