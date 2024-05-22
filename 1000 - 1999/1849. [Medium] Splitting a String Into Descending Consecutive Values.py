# https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        @cache 
        def helper(prev, idx):
            if idx == n: 
                return True 
            
            else: 
                tmp = ""
                
                for i in range(idx, n):
                    tmp += s[i]
                    
                    if int(tmp) + 1 == prev: 
                        if helper(prev - 1, i + 1):
                            return True 
                    
                return False 
        
        n = len(s)
        
        tmp = ""
        
        for (i, char) in enumerate(s[: n - 1]):
            tmp += char 
            
            if helper(int(tmp), i + 1):
                return True 
            
        return False
        
        
