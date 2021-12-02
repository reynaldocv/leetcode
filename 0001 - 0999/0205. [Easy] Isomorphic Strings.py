# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        dicS, dicT = {}, {}
        idx = 0
        for i in s: 
            if i not in dicS:
                dicS[i] = str(idx)
                idx += 1
        idx = 0
        for i in t: 
            if i not in dicT:
                dicT[i] = str(idx)
                idx += 1
                
        for i in dicS: 
            s = s.replace(i, dicS[i])
        for i in dicT: 
            t = t.replace(i, dicT[i])
        
        return s == t
        
