# https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        def recursive(s, num):
            if s == "": 
                return True
            else: 
                for i in range(1, len(s) + 1):
                    aux = int(s[:i])
                    if aux == num: 
                        if recursive(s[i:], num - 1):
                            return True
                return False
        
        for i in range(1, len(s)):
            num = int(s[:i])
            if num != 0: 
                if recursive(s[i:], num - 1):
                    return True
        
        return False
