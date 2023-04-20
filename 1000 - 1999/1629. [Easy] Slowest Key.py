# https://leetcode.com/problems/slowest-key/

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        n = len(releaseTimes) 
        
        ans = (releaseTimes[0], keysPressed[0])
        
        for i in range(1, n):
            ans = max(ans, (releaseTimes[i] - releaseTimes[i - 1], keysPressed[i]))
            
        return ans[1]
        
