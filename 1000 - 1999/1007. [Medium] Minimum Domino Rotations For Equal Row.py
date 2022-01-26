# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        ans = inf
        for val in range(1, 7):
            cntTops, cntBottoms = 0, 0
            go = True
            for i in range(n):
                if val == tops[i] or val == bottoms[i]:
                    cntTops += 1 if val == tops[i] else 0
                    cntBottoms += 1 if val == bottoms[i] else 0
                else: 
                    go = False
                    break 
                    
            if go: 
                ans = min(ans, cntTops, n - cntTops, cntBottoms, n - cntBottoms)
                
        return ans if ans != inf else -1
                    
            
                    
