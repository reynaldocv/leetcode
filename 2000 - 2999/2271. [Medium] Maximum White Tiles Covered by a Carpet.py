# https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/

class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        
        prefix = [0]
        ends = []
        for (a, b) in tiles: 
            prefix.append(prefix[-1] + b - a + 1)
            ends.append(b)
            
        n = len(ends)
        j = 0 
        
        ans = 0 
        
        for i in range(n):
            (start, _) = tiles[i]
            end = min(ends[-1], start + carpetLen - 1)
            
            while j < n and ends[j] < end: 
                j += 1 
                
            if tiles[j][0] > end: 
                ans = max(ans, prefix[j] - prefix[i])
            else: 
                ans = max(ans, prefix[j + 1] - prefix[i] - ends[j] + end)
            
        return ans
        
