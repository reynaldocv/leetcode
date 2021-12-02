# https://leetcode.com/problems/long-pressed-name/

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n, m, i, j = len(name), len(typed), 0, 0
        aux = ""
        while i < n and j < m:
            if name[i] == typed[j]:
                aux = name[i]
                i += 1
                j += 1
            else:
                if typed[j] == aux:
                    j += 1
                else:
                    return False
        
        if i == n:
            go = True
            for i in typed[j:]:
                if aux != i:
                    return False
            return True
        return False
                
