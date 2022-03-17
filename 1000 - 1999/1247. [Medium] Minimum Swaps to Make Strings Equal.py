# https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = 0
        yx = 0

        n = len(s1)
        
        for i in range(n):
            if s1[i] != s2[i]:
                if s1[i] == "x":
                    xy += 1
                else:
                    yx += 1
                    
        if (xy + yx) % 2 != 0:
            return -1
        else:
            return (xy//2 + xy % 2) + (yx//2 + yx % 2)
        
            
        
                
