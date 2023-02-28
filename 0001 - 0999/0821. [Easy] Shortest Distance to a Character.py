# https://leetcode.com/problems/shortest-distance-to-a-character/

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        
        ans = [n for _ in range(n)]
        
        distance = n
        
        for (i, char) in enumerate(s):
            if char == c:
                distance = 0 
            else:
                distance += 1
                
            ans[i] = distance
            
        distance = n
        
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                distance = 0 
            else:
                distance += 1
            
            ans[i] = min(ans[i], distance)
            
        return ans
                
            
