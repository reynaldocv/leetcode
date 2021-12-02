# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        auxs = [i for i in s]
        auxt = [i for i in t]
        auxs.sort()
        auxt.sort()
        return "".join(auxs) == "".join(auxt)
        
