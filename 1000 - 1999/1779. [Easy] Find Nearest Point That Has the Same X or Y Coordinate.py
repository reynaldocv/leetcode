# https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ans = (inf, -1)
        
        for (i, (p, q)) in enumerate(points): 
            if p == x or q == y: 
                ans = min(ans, (abs(p - x) + abs(q - y), i))
                
        return ans[1]
                
