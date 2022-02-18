# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MOD = 10**9 + 7
        
        horizontalCuts.sort()
        horizontalCuts.insert(0, 0)
        horizontalCuts.append(h)
        
        verticalCuts.sort()
        verticalCuts.insert(0, 0)
        verticalCuts.append(w)
        
        n, m = len(horizontalCuts), len(verticalCuts)
        
        maxWidth = 0 
        
        for i in range(n - 1):
            maxWidth = max(maxWidth, horizontalCuts[i + 1] - horizontalCuts[i])
            
        maxHeight = 0 
        
        for i in range(m - 1):
            maxHeight = max(maxHeight, verticalCuts[i + 1] - verticalCuts[i])
            
        return maxWidth*maxHeight % MOD
