# https://leetcode.com/problems/long-pressed-name/

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name += "$"
        typed += "$"
        
        m, n = len(name), len(typed)
        
        i = 0
        j = 0
                
        while i < m and j < n:
            if name[i] == typed[j]:                
                i += 1
                j += 1
                
            else:
                if 0 <= i - 1 and name[i - 1] == typed[j]:
                    j += 1
                    
                else:
                    return False
        
        return j == n
