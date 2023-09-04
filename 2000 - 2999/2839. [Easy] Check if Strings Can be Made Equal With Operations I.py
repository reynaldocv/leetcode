# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        even1 = [s1[0], s1[2]]
        even2 = [s2[0], s2[2]]
        
        return sorted(s1) == sorted(s2) and sorted(even1) == sorted(even2)
        
        
        
