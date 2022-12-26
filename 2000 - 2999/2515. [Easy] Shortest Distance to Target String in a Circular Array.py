# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/

class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        ans = inf 
        
        n = len(words)
        
        for (i, word) in enumerate(words):
            if word == target: 
                distance = abs(startIndex - i)
                
                ans = min(ans, distance, n - distance)
                
        return -1 if ans == inf else ans 
        
