# https://leetcode.com/problems/shortest-distance-to-a-character/

class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        l = len(S)
        ans = [l for i in range(l)]
        aux = l
        for i in range(l):
            if S[i] == C:
                ans[i] = 0
            else:
                ans[i] = ans[i - 1] + 1
        for i in range(l - 2, -1, -1):
            if S[i] != C:                
                ans[i] = min(ans[i], ans[i + 1] + 1)
        
        return ans
                
            
