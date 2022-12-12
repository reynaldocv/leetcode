# https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s) 
        
        tmp = s 
        
        for _ in range(n):
            tmp = tmp[-1] + tmp[: -1]
            
            if tmp == goal:
                return True 
            
        return False 
