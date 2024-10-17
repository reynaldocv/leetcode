# https://leetcode.com/problems/maximum-swap/ 

class Solution:
    def maximumSwap(self, num: int) -> int:
        n = len(str(num))
        
        chars = []
        maxElems = []
        
        for (ith, char) in enumerate(str(num)):
            chars.append(char)
            maxElems.append((char, ith))
        
        for i in range(n - 2, -1, -1):
            maxElems[i] = max(maxElems[i], maxElems[i + 1])
        
        for (ith, char) in enumerate(str(num)):
            (oldChar, jth) = maxElems[ith]
            
            if char != oldChar:                
                chars[jth] = char
                chars[ith] = oldChar
                
                break 
             
        return int("".join(chars))
