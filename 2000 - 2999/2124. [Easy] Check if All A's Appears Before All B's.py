# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

class Solution:
    def checkString(self, s: str) -> bool:
        index = [-1, -1]
        for (i, char) in enumerate(s):
            if char == "a":
                index[0] = i
            elif index[1] == -1:
                index[1] = i
                
        return index[0] < index[1] if index[1] != -1 else True
        
