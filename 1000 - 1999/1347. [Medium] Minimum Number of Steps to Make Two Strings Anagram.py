# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counterS, counterT = {}, {}
        for l in s: 
            counterS[l] = counterS.get(l, 0) + 1       
        
        for l in t: 
            if l in counterS: 
                counterT[l] = counterT.get(l, 0) + 1       
                
        common = 0 
        for key in counterT: 
            if key in counterS: 
                common += min(counterT[key], counterS[key])
        
        return len(s) - common
