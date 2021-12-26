# https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/

class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        m = len(s)
        
        moves = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}
        
        ans = [-1 for _ in range(m)]
        
        for i in range(m):
            x, y = startPos[0], startPos[1]
            idx = i
            dist = 0
            while idx < m and 0 <= x + moves[s[idx]][0] < n and 0 <= y + moves[s[idx]][1] < n: 
                x, y = x + moves[s[idx]][0], y + moves[s[idx]][1]                                
                dist += 1
                idx += 1
                
            ans[i] = dist
            
        return ans
