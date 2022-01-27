# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/

class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        counter = [0, 0]
        for (i, bit) in enumerate(s):
            counter[int(bit)] += 1 
        
        if abs(counter[0] - counter[1]) > 1: 
            return -1
                
        swaps1, swaps2 = 0, 0
        for i in range(0, n, 2):
            if s[i] != "0":
                swaps1 += 1 

        for i in range(0, n, 2):
            if s[i] != "1":
                swaps2 += 1 
                
        if counter[0] > counter[1]:
            return swaps1
        elif counter[1] > counter[0]:
            return swaps2
        else: 
            return min(swaps1, swaps2)

            
                
                
        
            
                
                
        
        
