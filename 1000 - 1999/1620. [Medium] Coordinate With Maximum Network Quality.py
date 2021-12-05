# https://leetcode.com/problems/coordinate-with-maximum-network-quality/

class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        r = radius
        maxX = max(x + r for (x, _, q) in towers)
        maxY = max(y + r for (_, y, q) in towers)
        
        quality = [[0 for _ in range(maxY + 1)] for _ in range(maxX + 1)]
        
        higher = 0 
        
        for (x, y, q) in towers: 
            for i in range(max(0, x - r), x + r + 1):
                for j in range(max(0, y - r), y + r + 1):
                    dist = (i - x)**2 + (j - y)**2
                    if r**2 >= dist:                        
                        quality[i][j] += int(q/(1 + dist**.5))
                        higher = max(higher, quality[i][j])
                                             
        ans = (inf, inf)
        for i in range(maxX + 1):
            for j in range(maxY + 1):
                if higher == quality[i][j]:
                    ans = min(ans, (i, j))
        
        return ans
        
