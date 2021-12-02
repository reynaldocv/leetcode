# https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        n = len(s)
        ans = True
        
        for j in range(n):                
            if s[0] == goal[j]:
                go = True
                for k in range(1, n):
                    if s[k] != goal[(j + k) % n]:
                        go = False
                        break
                if go: 
                    return True
        return False
