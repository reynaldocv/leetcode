# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        seen = defaultdict(lambda: 0)
        topCounter = defaultdict(lambda: 0)
        bottomCounter = defaultdict(lambda: 0)
        n = len(tops)
        
        for i in range(n):
            if tops[i] != bottoms[i]:                
                seen[tops[i]] += 1 
                seen[bottoms[i]] += 1 
            else: 
                seen[tops[i]] += 1 
                
            topCounter[tops[i]] += 1 
            bottomCounter[bottoms[i]] += 1
            
        ans = inf
        for key in seen: 
            if seen[key] == n: 
                ans = min(ans, n - topCounter[key])
                ans = min(ans, n - bottomCounter[key])
                
        return -1 if ans == inf else ans
                    
            
                    
