# https://leetcode.com/problems/check-distances-between-same-letters/

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        seen = {}
        index = {chr(ord("a") + i): i for i in range(26)}
        
        for (i, char) in enumerate(s):
            if char in seen: 
                dist = i - seen[char] - 1
                if dist != distance[index[char]]:
                    return False 
            else:
                seen[char] = i 
                
        return True
